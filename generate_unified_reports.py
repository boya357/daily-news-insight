#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一产业链日报格式生成器
基于液冷产业链深度研究报告模板，统一所有产业链日报格式
"""

import os
from datetime import datetime

# 标准HTML模板 - 绿色主题色 #4CAF50
STANDARD_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; background: #f5f7fa; color: #333; line-height: 1.6; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}
        .header {{ background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%); color: white; padding: 40px; border-radius: 16px; margin-bottom: 30px; box-shadow: 0 10px 40px rgba(76, 175, 80, 0.3); }}
        .header h1 {{ font-size: 2.5em; margin-bottom: 10px; }}
        .header .date {{ opacity: 0.9; font-size: 1.2em; }}
        .section {{ background: white; border-radius: 12px; padding: 30px; margin-bottom: 25px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); }}
        .section h2 {{ color: #4CAF50; font-size: 1.5em; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 2px solid #4CAF50; }}
        .market-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 20px 0; }}
        .market-card {{ background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%); color: white; padding: 20px; border-radius: 10px; text-align: center; }}
        .market-card .value {{ font-size: 1.8em; font-weight: bold; }}
        .market-card .label {{ opacity: 0.9; margin-top: 5px; }}
        .news-item {{ background: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 15px; border-left: 4px solid #4CAF50; }}
        .news-item h3 {{ color: #333; margin-bottom: 10px; }}
        .news-item .tag {{ display: inline-block; background: #4CAF50; color: white; padding: 3px 12px; border-radius: 20px; font-size: 0.85em; margin-right: 10px; }}
        .news-item .tag.hot {{ background: #ff6b6b; }}
        .news-item .tag.policy {{ background: #4ecdc4; }}
        .news-item .tag.tech {{ background: #f093fb; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ padding: 12px 15px; text-align: left; border-bottom: 1px solid #eee; }}
        th {{ background: #4CAF50; color: white; }}
        tr:hover {{ background: #f8f9fa; }}
        .warning {{ background: #fff3cd; border-left: 4px solid #ffc107; padding: 15px; border-radius: 8px; margin-top: 20px; }}
        .info-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }}
        .info-card {{ background: #f8f9fa; padding: 20px; border-radius: 10px; }}
        .info-card h4 {{ color: #4CAF50; margin-bottom: 15px; }}
        .trend-up {{ color: #22c55e; }}
        .trend-down {{ color: #ef4444; }}
        .footer {{ text-align: center; padding: 30px; color: #888; font-size: 0.9em; }}
        .chain-diagram {{ background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 25px; border-radius: 12px; margin: 20px 0; }}
        .chain-level {{ display: flex; justify-content: space-between; align-items: center; margin: 15px 0; padding: 15px; background: white; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
        .chain-level.upstream {{ border-left: 4px solid #2196F3; }}
        .chain-level.midstream {{ border-left: 4px solid #4CAF50; }}
        .chain-level.downstream {{ border-left: 4px solid #FF9800; }}
        .tech-card {{ background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 10px 0; border: 1px solid #e0e0e0; }}
        .tech-card h4 {{ color: #4CAF50; margin-bottom: 10px; }}
        .signal-tag {{ display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 0.8em; margin-left: 5px; }}
        .signal-tag.buy {{ background: #4CAF50; color: white; }}
        .signal-tag.sell {{ background: #ef4444; color: white; }}
        .signal-tag.hold {{ background: #ffc107; color: white; }}
        .signal-tag.reduced {{ background: #ff9800; color: white; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{icon} {main_title}</h1>
            <p class="date">📅 {date} | 龙空龙策略专用</p>
        </div>
        
        {content}
        
        <div class="section">
            <h2>⚠️ 风险提示</h2>
            <div class="warning">
                <strong>🔴 核心风险：</strong>
                <ul style="margin: 10px 20px;">
                    {risk_content}
                </ul>
            </div>
        </div>

        <div class="section">
            <h2>🔮 推理预判</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>📊 短期预判(1-3个月)</h4>
                    <ul style="margin-left: 20px;">
                        {short_term}
                    </ul>
                </div>
                <div class="info-card">
                    <h4>📈 中期预判(3-6个月)</h4>
                    <ul style="margin-left: 20px;">
                        {medium_term}
                    </ul>
                </div>
            </div>
            
            <div class="info-card" style="margin-top: 20px;">
                <h4>🎯 龙空龙策略建议</h4>
                {strategy_content}
            </div>
        </div>

        <div class="footer">
            <p>免责声明：本文内容仅供参考，不构成投资建议。股市有风险，投资需谨慎。</p>
            <p>数据来源：公开市场信息综合整理 | 生成时间：{gen_date}</p>
            <p>© 龙空龙策略专用报告 | {chain_name}产业链日报</p>
        </div>
    </div>
</body>
</html>
'''

def generate_standard_report(chain_name, icon, title, date, market_data, content_sections, risk_items, short_term_items, medium_term_items, strategy_text, output_path):
    """生成标准格式的产业链日报"""
    
    # 构建市场数据卡片
    market_cards = ""
    for data in market_data:
        market_cards += f'''                <div class="market-card">
                    <div class="value">{data['value']}</div>
                    <div class="label">{data['label']}</div>
                </div>
'''
    
    # 构建内容部分
    content = f'''
        <div class="section">
            <h2>📊 产业核心数据</h2>
            <div class="market-grid">
{market_cards}            </div>
        </div>
'''
    
    # 添加各个内容板块
    for section in content_sections:
        content += section
    
    # 构建风险内容
    risk_content = ""
    for risk in risk_items:
        risk_content += f"                    <li><strong>{risk}</strong></li>\n"
    
    # 构建短期预判
    short_term = ""
    for item in short_term_items:
        short_term += f"                        <li>{item}</li>\n"
    
    # 构建中期预判
    medium_term = ""
    for item in medium_term_items:
        medium_term += f"                        <li>{item}</li>\n"
    
    # 完整HTML
    html = STANDARD_TEMPLATE.format(
        title=title,
        icon=icon,
        main_title=chain_name,
        date=date,
        content=content,
        risk_content=risk_content,
        short_term=short_term,
        medium_term=medium_term,
        strategy_content=strategy_text,
        gen_date=datetime.now().strftime("%Y年%m月%d日 %H:%M"),
        chain_name=chain_name
    )
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ 生成完成: {output_path}")
    return html


def create_cpo_report():
    """生成CPO产业链标准日报"""
    chain_name = "CPO/光通信产业链"
    icon = "💡"
    title = "CPO/光通信产业链日报 2026"
    date = "2026年5月12日"
    
    market_data = [
        {"value": "+1.58%", "label": "国证通信指数强势上涨"},
        {"value": "+15.69%", "label": "吴通控股领涨成分股"},
        {"value": "+10.01%", "label": "德科立续创新高"},
        {"value": "7连涨", "label": "通信ETF冲击纪录"}
    ]
    
    content_sections = [
        '''
        <div class="section">
            <h2>⚡ 产业投资逻辑</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>🔥 第一性原理</h4>
                    <p style="margin: 10px 0;"><strong>AI算力三大瓶颈：</strong>功耗、带宽、时延。传统光模块功耗占比数据中心30%+，CPO将光引擎与芯片共封装，功耗降低50%、时延降低70%。</p>
                    <p style="margin: 10px 0;"><strong>政策强催化：</strong>工信部要求新建智算中心CPO适配比例≥60%，核心光配件国产化率≥70%。</p>
                </div>
                <div class="info-card">
                    <h4>🎯 三大驱动逻辑</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>AI芯片功耗飙升：</strong>GB200 NVL72功耗超130kW，传统光模块成最大瓶颈</li>
                        <li><strong>巨头全面倒向：</strong>英伟达、谷歌、微软加速CPO导入</li>
                        <li><strong>国内技术突破：</strong>3.2T CPO光引擎量产，良率达95%</li>
                    </ul>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>🗺️ 产业链全景图</h2>
            <div class="chain-diagram">
                <h3 style="color: #2E7D32; margin-bottom: 15px;">📍 光通信/CPO产业链上中下游</h3>
                <div class="chain-level upstream">
                    <div>
                        <strong>🔩 上游：核心材料与芯片</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            光芯片(源杰科技/长光华芯) → 硅光芯片 → 磷化铟材料 → VCSEL/DFB激光器 → 光纤预制棒(长飞光纤/亨通光电)
                        </p>
                    </div>
                </div>
                <div class="chain-level midstream">
                    <div>
                        <strong>⚙️ 中游：光器件与光模块</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            光迅科技/中际旭创/新易盛 → CPO光引擎(天孚通信/剑桥科技) → 1.6T/3.2T光模块 → 华为/英伟达生态
                        </p>
                    </div>
                </div>
                <div class="chain-level downstream">
                    <div>
                        <strong>🖥️ 下游：算力需求方</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            云厂商(阿里/腾讯/字节/百度) → AI训练集群 → 数据中心(万国数据/秦淮数据) → CSP(英伟达/谷歌/微软)
                        </p>
                    </div>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>💹 A股核心标的深度对比</h2>
            <h3 style="margin: 20px 0 15px;">🔥 第一梯队：光模块龙头</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心优势</th><th>核心客户</th><th>投资信号</th></tr>
                <tr>
                    <td>中际旭创</td>
                    <td>300308</td>
                    <td>全球光模块份额第一，1.6T/3.2T技术领先，市值破万亿</td>
                    <td>谷歌、亚马逊、英伟达</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
                <tr>
                    <td>新易盛</td>
                    <td>300502</td>
                    <td>1.6T光模块量产，CPO技术储备</td>
                    <td>微软、Meta、爱立信</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
                <tr>
                    <td>光迅科技</td>
                    <td>002281</td>
                    <td>国内光器件龙头，3.2T CPO模块送样</td>
                    <td>华为、中兴、烽火</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>华工科技</td>
                    <td>000988</td>
                    <td>3.2T CPO光引擎规模化量产</td>
                    <td>华为、阿里、百度</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
            </table>
            
            <h3 style="margin: 20px 0 15px;">⚡ 第二梯队：核心器件与材料</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心产品</th><th>投资信号</th></tr>
                <tr>
                    <td>天孚通信</td>
                    <td>688041</td>
                    <td>CPO光引擎核心器件，精密光学组件</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
                <tr>
                    <td>源杰科技</td>
                    <td>688498</td>
                    <td>25G/50G DFB激光器芯片国产替代</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>剑桥科技</td>
                    <td>603083</td>
                    <td>光模块代工+CPO布局</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
                <tr>
                    <td>太辰光</td>
                    <td>300570</td>
                    <td>光纤连接器，光无源器件</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
            </table>
        </div>
''',
        '''
        <div class="section">
            <h2>🎯 操作建议</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>📈 投资主线</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>核心配置：</strong>中际旭创(全球龙头)、新易盛(技术突破)</li>
                        <li><strong>弹性标的：</strong>华工科技(3.2T量产)、光迅科技(估值修复)</li>
                        <li><strong>潜伏标的：</strong>天孚通信(CPO核心器件)、源杰科技(芯片国产替代)</li>
                        <li><strong>材料补涨：</strong>长飞光纤(光纤涨价)、亨通光电(海缆+光通信)</li>
                    </ul>
                </div>
                <div class="info-card">
                    <h4>⚠️ 操作策略</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>买点：</strong>回调5%-10%后分批建仓</li>
                        <li><strong>止损：</strong>跌破买入价8%严格止损</li>
                        <li><strong>止盈：</strong>目标涨幅30-50%，分批兑现</li>
                        <li><strong>仓位：</strong>单票不超过总仓位15%</li>
                    </ul>
                </div>
            </div>
            
            <table>
                <tr><th>标的</th><th>股票代码</th><th>建议买点</th><th>止损位</th><th>目标价</th><th>逻辑</th></tr>
                <tr><td>中际旭创</td><td>300308</td><td>回调10%</td><td>看支撑</td><td>新高</td><td>全球份额第一+AI算力</td></tr>
                <tr><td>新易盛</td><td>300502</td><td>80-90元</td><td>70元</td><td>120元+</td><td>1.6T量产+CPO</td></tr>
                <tr><td>华工科技</td><td>000988</td><td>35-40元</td><td>30元</td><td>55元+</td><td>3.2T CPO量产</td></tr>
                <tr><td>光迅科技</td><td>002281</td><td>25-28元</td><td>22元</td><td>40元+</td><td>CPO送样+估值修复</td></tr>
            </table>
        </div>
''',
        '''
        <div class="section">
            <h2>🚀 核心催化剂</h2>
            <div class="news-item">
                <span class="tag policy">政策催化</span>
                <h3>工信部强制落地：新建智算中心CPO适配比例≥60%</h3>
                <p>核心光配件国产化率≥70%，将CPO从"可选项"变为"必选项"。</p>
            </div>
            <div class="news-item">
                <span class="tag hot">订单爆发</span>
                <h3>英伟达联合康宁：5亿美元战略投资+10倍产能扩张</h3>
                <p>印证AI算力对底层光通信资源的刚性需求，CPO加速落地。</p>
            </div>
            <div class="news-item">
                <span class="tag tech">技术突破</span>
                <h3>3.2T CPO光引擎量产+良率突破95%</h3>
                <p>国内企业自研硅光芯片良率达95%，对准精度达±0.05微米。</p>
            </div>
            <div class="news-item">
                <span class="tag">价格暴涨</span>
                <h3>G.652.D光纤价格暴涨：25元→105元/芯公里</h3>
                <p>出口单价同比上涨194.6%，量价齐升逻辑持续。</p>
            </div>
        </div>
'''
    ]
    
    risk_items = [
        "技术路线变更：CPO与LPO等技术路线竞争，结果不确定",
        "价格战风险：光模块行业竞争激烈，龙头份额竞争压制毛利",
        "中美贸易摩擦：核心芯片、设备出口管制影响供应链",
        "短期涨幅过大：部分个股乖离率偏高，需等待回调机会",
        "订单兑现风险：AI资本开支周期性波动可能影响需求"
    ]
    
    short_term_items = [
        "光模块板块震荡上行，个股分化加剧",
        "中际旭创、新易盛等核心标的回调后二次启动",
        "CPO量产消息持续催化，国产替代加速",
        "光纤价格持续上涨，业绩兑现期关注业绩超预期标的"
    ]
    
    medium_term_items = [
        "英伟达GB200 NVL72量产带动CPO需求爆发",
        "工信部政策倒逼下新建智算中心集中采购CPO",
        "国内厂商1.6T/3.2T光模块产能释放，业绩进入高速增长通道",
        "光通信产业链从'可选'变'必选'，景气度持续上行"
    ]
    
    strategy_content = '''
                <p style="margin: 10px 0;"><strong>核心标的：</strong>中际旭创(底仓配置)+新易盛(弹性进攻)+华工科技(技术突破)</p>
                <p style="margin: 10px 0;"><strong>操作节奏：</strong>回调低吸为主，不追高；分批建仓；严格止损</p>
                <p style="margin: 10px 0;"><strong>预期收益：</strong>龙头标的2026年上涨30-50%；业绩兑现期(2026H2)或迎主升浪</p>
    '''
    
    output_path = "./docs/reports/CPO产业链/CPO产业链标准日报.html"
    return generate_standard_report(chain_name, icon, title, date, market_data, content_sections, risk_items, short_term_items, medium_term_items, strategy_content, output_path)


def create_storage_report():
    """生成存储产业链标准日报"""
    chain_name = "存储产业链"
    icon = "💾"
    title = "存储产业链日报 2026"
    date = "2026年5月12日"
    
    market_data = [
        {"value": "+18.52%", "label": "澜起科技创历史新高"},
        {"value": "+15.97%", "label": "江波龙创历史新高"},
        {"value": "+280%", "label": "企业级SSD季度涨幅"},
        {"value": "+500%", "label": "HBM季度涨幅"}
    ]
    
    content_sections = [
        '''
        <div class="section">
            <h2>⚡ 产业投资逻辑</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>🔥 第一性原理</h4>
                    <p style="margin: 10px 0;"><strong>AI算力三大支柱：</strong>算力(GPU)、存力(HBM)、运力(光通信)。HBM作为AI GPU显存主流方案，需求与算力同步爆发。</p>
                    <p style="margin: 10px 0;"><strong>存储超级周期：</strong>2026年全球DRAM供需缺口4.9%，NAND缺口4.2%，HBM缺口5.1%，均为2011年以来最高水平。</p>
                </div>
                <div class="info-card">
                    <h4>🎯 三大驱动逻辑</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>AI芯片需求爆发：</strong>H100/H200/B100/GB200全面采用HBM</li>
                        <li><strong>原厂控量提价：</strong>三星、SK海力士、美光全面锁价</li>
                        <li><strong>国产替代空间：</strong>长江存储进入卖方市场，份额持续扩张</li>
                    </ul>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>🗺️ 产业链全景图</h2>
            <div class="chain-diagram">
                <h3 style="color: #2E7D32; margin-bottom: 15px;">📍 存储产业链上中下游</h3>
                <div class="chain-level upstream">
                    <div>
                        <strong>🔩 上游：存储芯片与材料</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            DRAM/NAND芯片(三星/ SK海力士/美光/长江存储) → HBM堆叠 → 硅晶圆(沪硅产业) → 靶材(江丰电子) → 光刻胶(南大光电)
                        </p>
                    </div>
                </div>
                <div class="chain-level midstream">
                    <div>
                        <strong>⚙️ 中游：存储模组与封装</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            模组厂(江波龙/佰维存储/朗科科技) → 封测(通富微电/长电科技) → 主控芯片(得一微/英韧科技) → DDR5(澜起科技/聚辰股份)
                        </p>
                    </div>
                </div>
                <div class="chain-level downstream">
                    <div>
                        <strong>🖥️ 下游：算力需求方</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            AI服务器(英伟达/AMD) → 云厂商(阿里/腾讯/字节/百度) → 数据中心 → 消费电子(手机/PC)
                        </p>
                    </div>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>💹 A股核心标的深度对比</h2>
            <h3 style="margin: 20px 0 15px;">🔥 第一梯队：存储龙头</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心优势</th><th>核心客户</th><th>投资信号</th></tr>
                <tr>
                    <td>澜起科技</td>
                    <td>688008</td>
                    <td>DDR5接口芯片全球第三，PC服务器内存龙头</td>
                    <td>英特尔、三星、阿里云</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
                <tr>
                    <td>江波龙</td>
                    <td>301308</td>
                    <td>嵌入式存储份额第一，Lexar品牌国际化</td>
                    <td>阿里、字节、华为</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
                <tr>
                    <td>佰维存储</td>
                    <td>688525</td>
                    <td>嵌入式存储核心供应商，国产替代加速</td>
                    <td>华为、小米、OPPO</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>兆易创新</td>
                    <td>603986</td>
                    <td>Nor Flash全球第三，MCU+DRAM三线布局</td>
                    <td>苹果、三星、华为</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
            </table>
            
            <h3 style="margin: 20px 0 15px;">⚡ 第二梯队：封装与设备</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心产品</th><th>投资信号</th></tr>
                <tr>
                    <td>通富微电</td>
                    <td>002156</td>
                    <td>先进封装，HBM/AI芯片封测</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>长电科技</td>
                    <td>600584</td>
                    <td>封测龙头，2.5D/3D封装布局</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
                <tr>
                    <td>长川科技</td>
                    <td>300604</td>
                    <td>存储芯片测试设备</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
            </table>
        </div>
''',
        '''
        <div class="section">
            <h2>📈 供需格局与涨价逻辑</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>🔺 需求端爆发</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>AI芯片全面上量：</strong>H100/H200/B100/GB200全部采用HBM</li>
                        <li><strong>企业级SSD需求：</strong>Q1涨幅280%，数据中心扩容</li>
                        <li><strong>DDR5升级换代：</strong>PC服务器换机潮</li>
                    </ul>
                </div>
                <div class="info-card">
                    <h4>🔻 供给端瓶颈</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>原厂控量：</strong>三星/SK海力士/美光全面锁价</li>
                        <li><strong>产能扩张慢：</strong>HBM产线建设周期18个月以上</li>
                        <li><strong>HBM良率低：</strong>3层/4层堆叠良率仍在爬坡</li>
                    </ul>
                </div>
            </div>
            <table>
                <tr><th>品类</th><th>Q1涨幅</th><th>Q2预测涨幅</th><th>全年预测</th></tr>
                <tr><td>DRAM合约价</td><td>+90-95%</td><td>+58-63%</td><td>+88%(高盛:250-280%)</td></tr>
                <tr><td>NAND合约价</td><td>+55-60%</td><td>+70-75%</td><td>+74%(高盛:200-250%)</td></tr>
                <tr><td>DDR5现货价</td><td>+91%</td><td>继续上涨</td><td>全年高位</td></tr>
                <tr><td>企业级SSD</td><td>+280%</td><td>—</td><td>持续紧张</td></tr>
                <tr><td>HBM价格</td><td>+500%</td><td>供不应求</td><td>持续高位</td></tr>
            </table>
        </div>
''',
        '''
        <div class="section">
            <h2>🎯 操作建议</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>📈 投资主线</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>核心配置：</strong>澜起科技(DDR5龙头)、江波龙(存储模组)</li>
                        <li><strong>弹性标的：</strong>佰维存储(国产替代)、兆易创新(Nor Flash)</li>
                        <li><strong>潜伏标的：</strong>通富微电(HBM封测)、长川科技(测试设备)</li>
                    </ul>
                </div>
                <div class="info-card">
                    <h4>⚠️ 操作策略</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>买点：</strong>回调10-15%后分批建仓</li>
                        <li><strong>止损：</strong>跌破买入价8%严格止损</li>
                        <li><strong>止盈：</strong>目标涨幅50-80%，分批兑现</li>
                    </ul>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>🚀 核心催化剂</h2>
            <div class="news-item">
                <span class="tag policy">原厂业绩</span>
                <h3>SK海力士Q1营业利润同比+405%</h3>
                <p>HBM市占率全球第一，全年产能100%排产无余量可追加。</p>
            </div>
            <div class="news-item">
                <span class="tag hot">三星电子</span>
                <h3>三星Q1营业利润同比+756%</h3>
                <p>HBM产能已全部售罄，2027年订单已批量提前预订。</p>
            </div>
            <div class="news-item">
                <span class="tag tech">国产突破</span>
                <h3>长江存储进入"先款排产"卖方市场</h3>
                <p>Q1营收超200亿同比翻倍，NAND全球份额超13%。</p>
            </div>
            <div class="news-item">
                <span class="tag">涨价持续</span>
                <h3>存储超级周期延续至2027年</h3>
                <p>供需缺口持续，价格无下行压力。</p>
            </div>
        </div>
'''
    ]
    
    risk_items = [
        "原厂产能扩张：三星/SK海力士扩产可能导致供需逆转",
        "技术路线变更：新型存储技术可能替代传统DRAM/NAND",
        "贸易摩擦风险：美国对华半导体出口管制影响设备采购",
        "短期涨幅过大：部分个股乖离率偏高，需等待回调",
        "客户集中风险：大客户依赖度较高"
    ]
    
    short_term_items = [
        "存储板块强势不改，个股轮动上涨",
        "澜起科技、江波龙等核心标的持续创新高",
        "原厂涨价消息持续催化，业绩兑现期关注超预期标的",
        "DDR5渗透率提升带动相关标的业绩爆发"
    ]
    
    medium_term_items = [
        "AI GPU全面上量，HBM需求与算力同步爆发",
        "存储超级周期延续，价格高位运行至2027年",
        "国产替代加速，长江存储份额持续扩张",
        "龙头厂商业绩进入高速增长通道"
    ]
    
    strategy_content = '''
                <p style="margin: 10px 0;"><strong>核心标的：</strong>澜起科技(底仓配置)+江波龙(存储模组)+佰维存储(国产替代)</p>
                <p style="margin: 10px 0;"><strong>操作节奏：</strong>回调低吸为主，不追高；分批建仓；严格止损</p>
                <p style="margin: 10px 0;"><strong>预期收益：</strong>龙头标的2026年上涨50-100%；业绩兑现期(2026H2)或迎主升浪</p>
    '''
    
    output_path = "./docs/reports/存储产业链/存储产业链标准日报.html"
    return generate_standard_report(chain_name, icon, title, date, market_data, content_sections, risk_items, short_term_items, medium_term_items, strategy_content, output_path)


def create_commercial_space_report():
    """生成商业航天产业链标准日报"""
    chain_name = "商业航天产业链"
    icon = "🚀"
    title = "商业航天产业链日报 2026"
    date = "2026年5月12日"
    
    market_data = [
        {"value": "朱雀2e", "label": "5月13日择机发射"},
        {"value": "朱雀三号遥二", "label": "5月18-20日择机发射"},
        {"value": "长征十号乙", "label": "5月中下旬文昌首飞"},
        {"value": "GW星座", "label": "50-60%由中国卫星制造"}
    ]
    
    content_sections = [
        '''
        <div class="section">
            <h2>⚡ 产业投资逻辑</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>🔥 第一性原理</h4>
                    <p style="margin: 10px 0;"><strong>卫星互联网战略价值：</strong>GW星座计划1.3万颗+星链1.2万颗，低轨轨道资源稀缺，各国加速布局。</p>
                    <p style="margin: 10px 0;"><strong>可回收技术降本：</strong>火箭回收使发射成本降低70%，商业化拐点到来。</p>
                </div>
                <div class="info-card">
                    <h4>🎯 三大驱动逻辑</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>政策强力支持：</strong>《商业航天标准体系(1.0版)》发布，千余项标准覆盖全链条</li>
                        <li><strong>发射密度爆发：</strong>2026年商业发射预计突破150次</li>
                        <li><strong>国产替代加速：</strong>推力室等核心零部件实现自主可控</li>
                    </ul>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>🗺️ 产业链全景图</h2>
            <div class="chain-diagram">
                <h3 style="color: #2E7D32; margin-bottom: 15px;">📍 商业航天产业链上中下游</h3>
                <div class="chain-level upstream">
                    <div>
                        <strong>🔩 上游：材料与零部件</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            复合材料(斯瑞新材) → 发动机推力室 → 特种合金 → 航空复材(广联航空) → 启动器(航天晨光)
                        </p>
                    </div>
                </div>
                <div class="chain-level midstream">
                    <div>
                        <strong>⚙️ 中游：火箭与卫星制造</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            火箭总装(蓝箭航天/星际荣耀/天兵科技) → 卫星制造(中国卫星/上海垣信) → 发动机(航天动力) → 测控(航天驭星)
                        </p>
                    </div>
                </div>
                <div class="chain-level downstream">
                    <div>
                        <strong>🖥️ 下游：卫星应用</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            卫星互联网 → 遥感星座 → 通信服务(中国卫通) → 导航增强 → 6G技术试验
                        </p>
                    </div>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>💹 A股核心标的深度对比</h2>
            <h3 style="margin: 20px 0 15px;">🔥 第一梯队：核心标的</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心优势</th><th>核心客户</th><th>投资信号</th></tr>
                <tr>
                    <td>中国卫星</td>
                    <td>600118</td>
                    <td>A股唯一小卫星总装上市公司，承担GW星座50-60%任务</td>
                    <td>国家航天局、GW星座</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
                <tr>
                    <td>斯瑞新材</td>
                    <td>688102</td>
                    <td>发动机推力室内壁亚洲唯一，朱雀三号全批次独家供货</td>
                    <td>蓝箭航天、航天科技</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>航宇科技</td>
                    <td>688239</td>
                    <td>航空航天环形锻件龙头，在手订单60亿+</td>
                    <td>多家火箭厂商</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
                <tr>
                    <td>金风科技</td>
                    <td>002202</td>
                    <td>蓝箭航天重要股东，持股10.1%</td>
                    <td>蓝箭航天</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
            </table>
            
            <h3 style="margin: 20px 0 15px;">⚡ 第二梯队：配套企业</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心产品</th><th>投资信号</th></tr>
                <tr>
                    <td>广联航空</td>
                    <td>300900</td>
                    <td>航空/航天复合材料</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>航天晨光</td>
                    <td>600501</td>
                    <td>特种装备、压力容器</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
                <tr>
                    <td>中国卫通</td>
                    <td>601698</td>
                    <td>卫星通信运营</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
            </table>
        </div>
''',
        '''
        <div class="section">
            <h2>🎯 操作建议</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>📈 投资主线</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>核心配置：</strong>中国卫星(国家队绝对龙头)</li>
                        <li><strong>弹性标的：</strong>斯瑞新材(朱雀三号独家供货)</li>
                        <li><strong>潜伏标的：</strong>航宇科技(环形锻件龙头)</li>
                    </ul>
                </div>
                <div class="info-card">
                    <h4>⚠️ 操作策略</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>买点：</strong>发射节点前回调低吸</li>
                        <li><strong>止损：</strong>跌破买入价10%严格止损</li>
                        <li><strong>止盈：</strong>发射成功后分批兑现</li>
                    </ul>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>🚀 核心催化剂</h2>
            <div class="news-item">
                <span class="tag hot">发射催化</span>
                <h3>朱雀2e：5月13日择机发射</h3>
                <p>蓝箭航天IPO关键验证，金风科技参股10.1%。</p>
            </div>
            <div class="news-item">
                <span class="tag hot">发射催化</span>
                <h3>朱雀三号遥二：5月18-20日择机发射</h3>
                <p>二次回收测试，斯瑞新材锁定全批次独家供货。</p>
            </div>
            <div class="news-item">
                <span class="tag policy">国家队</span>
                <h3>长征十号乙：5月中下旬文昌首飞</h3>
                <p>全球首创海上网系回收技术。</p>
            </div>
            <div class="news-item">
                <span class="tag policy">政策催化</span>
                <h3>《商业航天标准体系(1.0版)》正式发布</h3>
                <p>覆盖"箭、星、场、用、治"全链条千余项标准。</p>
            </div>
        </div>
'''
    ]
    
    risk_items = [
        "发射失败风险：火箭技术仍在验证期，发射存在不确定性",
        "技术路线变更：可回收技术路线竞争，结果不确定",
        "订单兑现周期长：商业航天从订单到业绩转化需要2-3年",
        "政策支持不及预期：商业航天政策力度可能低于预期",
        "估值过高风险：部分标的估值偏高"
    ]
    
    short_term_items = [
        "5月发射密集期，关注朱雀2e、朱雀三号遥二、长征十号乙发射节点",
        "斯瑞新材、中国卫星等核心标的随发射节点波动",
        "武汉国资32.99亿入股航天科工火箭，行业资本化加速",
        "天舟十号成功发射，航天主题持续活跃"
    ]
    
    medium_term_items = [
        "2026年商业发射预计突破150次，产业链进入业绩兑现期",
        "GW星座加速部署，中国卫星等承担50-60%制造任务",
        "可回收技术成熟后，发射成本降低70%，商业化加速",
        "商业航天标准体系建立，行业规范化发展拐点到来"
    ]
    
    strategy_content = '''
                <p style="margin: 10px 0;"><strong>核心标的：</strong>中国卫星(底仓配置)+斯瑞新材(弹性进攻)</p>
                <p style="margin: 10px 0;"><strong>操作节奏：</strong>发射节点前布局，回调低吸；发射成功后分批兑现；严格止损</p>
                <p style="margin: 10px 0;"><strong>预期收益：</strong>发射成功催化短期上涨20-30%；长期看GW星座部署带来业绩爆发</p>
    '''
    
    output_path = "./repo_temp/docs/reports/商业航天日报/商业航天产业链标准日报.html"
    return generate_standard_report(chain_name, icon, title, date, market_data, content_sections, risk_items, short_term_items, medium_term_items, strategy_content, output_path)


def create_copper_foil_report():
    """生成铜箔产业链标准日报"""
    chain_name = "铜箔产业链"
    icon = "🟠"
    title = "铜箔产业链日报 2026"
    date = "2026年5月12日"
    
    market_data = [
        {"value": "106,745元/吨", "label": "沪铜主连(+2250元)"},
        {"value": "38-40万元/吨", "label": "HVLP高端铜箔"},
        {"value": "134,000元/吨", "label": "4.5μm锂电铜箔"},
        {"value": ">90%", "label": "行业开工率"}
    ]
    
    content_sections = [
        '''
        <div class="section">
            <h2>⚡ 产业投资逻辑</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>🔥 第一性原理</h4>
                    <p style="margin: 10px 0;"><strong>AI服务器PCB价值量3-5倍：</strong>AI服务器PCB层数从10层→20-30层，铜箔用量增加50%以上。</p>
                    <p style="margin: 10px 0;"><strong>高频高速铜箔刚需：</strong>112G/224G SerDes标准要求Ultra Low Loss铜箔，HVLP供需缺口48%。</p>
                </div>
                <div class="info-card">
                    <h4>🎯 三大驱动逻辑</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>AI服务器需求爆发：</strong>GB200/H200带动高端铜箔需求激增</li>
                        <li><strong>铜价上涨传导：</strong>沪铜突破10.6万/吨，成本推动涨价</li>
                        <li><strong>高端产能瓶颈：</strong>HVLP全球产能仅1200吨/月，缺口超48%</li>
                    </ul>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>🗺️ 产业链全景图</h2>
            <div class="chain-diagram">
                <h3 style="color: #2E7D32; margin-bottom: 15px;">📍 铜箔/覆铜板产业链上中下游</h3>
                <div class="chain-level upstream">
                    <div>
                        <strong>🔩 上游：铜矿与冶炼</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            铜矿(紫金矿业/洛阳钼业) → 精铜冶炼 → 电解铜(106,745元/吨) → 铜箔加工
                        </p>
                    </div>
                </div>
                <div class="chain-level midstream">
                    <div>
                        <strong>⚙️ 中游：铜箔与覆铜板</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            铜箔(诺德股份/嘉元科技) → 覆铜板(生益科技/南亚新材/华正新材) → PCB(鹏鼎控股/东山精密)
                        </p>
                    </div>
                </div>
                <div class="chain-level downstream">
                    <div>
                        <strong>🖥️ 下游：AI服务器与消费电子</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            AI服务器(浪潮信息/华为) → 交换机/路由器 → 消费电子(苹果/华为) → 汽车电子
                        </p>
                    </div>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>💹 A股核心标的深度对比</h2>
            <h3 style="margin: 20px 0 15px;">🔥 第一梯队：覆铜板龙头</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心优势</th><th>核心客户</th><th>投资信号</th></tr>
                <tr>
                    <td>生益科技</td>
                    <td>600183</td>
                    <td>覆铜板份额全球第二，高端产品占比提升</td>
                    <td>华为、苹果、特斯拉</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
                <tr>
                    <td>南亚新材</td>
                    <td>688188</td>
                    <td>覆铜板核心标的，持续创新高</td>
                    <td>华为、中兴、比亚迪</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
                <tr>
                    <td>华正新材</td>
                    <td>603186</td>
                    <td>高端覆铜板产能扩张</td>
                    <td>多家PCB厂商</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
            </table>
            
            <h3 style="margin: 20px 0 15px;">⚡ 第二梯队：铜箔与PCB</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心产品</th><th>投资信号</th></tr>
                <tr>
                    <td>诺德股份</td>
                    <td>600110</td>
                    <td>锂电铜箔龙头，6μm/4.5μm量产</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>嘉元科技</td>
                    <td>688388</td>
                    <td>高性能锂电铜箔</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
                <tr>
                    <td>鹏鼎控股</td>
                    <td>002938</td>
                    <td>PCB全球第一，苹果核心供应商</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
            </table>
        </div>
''',
        '''
        <div class="section">
            <h2>📈 供需格局与涨价逻辑</h2>
            <table>
                <tr><th>品类</th><th>当前价格</th><th>趋势</th><th>供需状态</th></tr>
                <tr><td>沪铜主连</td><td>106,745元/吨</td><td class="trend-up">↑ +2250元/日</td><td>供给刚性</td></tr>
                <tr><td>HVLP高端铜箔</td><td>38-40万元/吨</td><td class="trend-up">↑ 持续涨价</td><td>缺口48%</td></tr>
                <tr><td>4.5μm锂电铜箔</td><td>134,000元/吨</td><td class="trend-up">↑ +1500元</td><td>供不应求</td></tr>
                <tr><td>高端覆铜板</td><td>持续涨价</td><td class="trend-up">↑ +65%</td><td>排至2027年</td></tr>
                <tr><td>普通电子布</td><td>6.5元/米</td><td class="trend-up">↑ +55%</td><td>供需紧张</td></tr>
            </table>
        </div>
''',
        '''
        <div class="section">
            <h2>🎯 操作建议</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>📈 投资主线</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>核心配置：</strong>生益科技(覆铜板龙头)、南亚新材(持续新高)</li>
                        <li><strong>弹性标的：</strong>华正新材(高端产能扩张)、诺德股份(铜箔涨价)</li>
                        <li><strong>潜伏标的：</strong>鹏鼎控股(PCB份额第一)</li>
                    </ul>
                </div>
                <div class="info-card">
                    <h4>⚠️ 操作策略</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>买点：</strong>回调5-8%后分批建仓</li>
                        <li><strong>止损：</strong>跌破买入价8%严格止损</li>
                        <li><strong>止盈：</strong>目标涨幅30-50%，分批兑现</li>
                    </ul>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>🚀 核心催化剂</h2>
            <div class="news-item">
                <span class="tag hot">涨价</span>
                <h3>铜价突破10.6万/吨：单日暴涨2250元</h3>
                <p>AI服务器需求爆发+供给刚性约束，机构预计铜价冲击12,000-13,500美元/吨。</p>
            </div>
            <div class="news-item">
                <span class="tag hot">供需紧张</span>
                <h3>HVLP高端铜箔缺口48%：英伟达单月需求超全球产能</h3>
                <p>全球月产能1200吨，英伟达单月需求1900吨，交期3-6个月。</p>
            </div>
            <div class="news-item">
                <span class="tag policy">涨价</span>
                <h3>PCB四大材料全线涨价：覆铜板累计涨幅超40%</h3>
                <p>高端M8/M9涨幅65%，交货期拉长至4-6周，高端排至2027年。</p>
            </div>
        </div>
'''
    ]
    
    risk_items = [
        "铜价波动风险：铜价受宏观经济影响大，可能回调",
        "产能扩张过快：多家企业扩产可能导致供需逆转",
        "技术替代风险：新材料可能替代传统铜箔",
        "下游需求不及预期：AI服务器出货量可能低于预期",
        "短期涨幅过大：部分个股乖离率偏高"
    ]
    
    short_term_items = [
        "PCB板块强势不改，方邦股份等持续创新高",
        "铜价持续上涨，成本推动逻辑延续",
        "覆铜板交货期拉长，高端产品排至2027年",
        "高频高速铜箔供需缺口持续，涨价趋势明确"
    ]
    
    medium_term_items = [
        "AI服务器PCB价值量是普通服务器3-5倍，铜箔需求持续爆发",
        "HVLP高端铜箔供需缺口48%，涨价趋势延续至2027年",
        "覆铜板四大材料涨价传导顺畅，龙头厂商量价齐升",
        "行业集中度提升，龙头厂商受益于供给侧改革"
    ]
    
    strategy_content = '''
                <p style="margin: 10px 0;"><strong>核心标的：</strong>生益科技(底仓配置)+南亚新材(弹性进攻)+诺德股份(铜箔涨价)</p>
                <p style="margin: 10px 0;"><strong>操作节奏：</strong>回调低吸为主，不追高；关注铜价走势；严格止损</p>
                <p style="margin: 10px 0;"><strong>预期收益：</strong>龙头标的2026年上涨30-50%；涨价周期延续至2027年</p>
    '''
    
    output_path = "./docs/reports/铜箔产业链/铜箔产业链标准日报.html"
    return generate_standard_report(chain_name, icon, title, date, market_data, content_sections, risk_items, short_term_items, medium_term_items, strategy_content, output_path)


def create_helium_report():
    """生成氦气产业链标准日报"""
    chain_name = "氦气产业链"
    icon = "🔴"
    title = "氦气产业链日报 2026"
    date = "2026年5月12日"
    
    market_data = [
        {"value": "520-560元/m³", "label": "工业级管束氦(5N)"},
        {"value": "3800-4500元/瓶", "label": "40L瓶装高纯氦"},
        {"value": "3800-4200元/m³", "label": "电子级氦气(6N)"},
        {"value": "+45-60%", "label": "较4月底涨幅"}
    ]
    
    content_sections = [
        '''
        <div class="section">
            <h2>⚡ 产业投资逻辑</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>🔥 第一性原理</h4>
                    <p style="margin: 10px 0;"><strong>氦气不可替代：</strong>半导体制造(光刻机、刻蚀机)、医疗MRI、数据中心散热、航天发射均离不开氦气。</p>
                    <p style="margin: 10px 0;"><strong>资源稀缺性：</strong>全球氦气储量有限，主要分布在美国、卡塔尔、俄罗斯，供应高度集中。</p>
                </div>
                <div class="info-card">
                    <h4>🎯 三大驱动逻辑</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>地缘政治危机：</strong>卡塔尔+俄罗斯双重断供，全球40%产能中断</li>
                        <li><strong>AI算力需求：</strong>数据中心液冷散热需求激增</li>
                        <li><strong>国产替代加速：</strong>BOG提氦技术突破，成本仅为进口1/3</li>
                    </ul>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>🗺️ 产业链全景图</h2>
            <div class="chain-diagram">
                <h3 style="color: #2E7D32; margin-bottom: 15px;">📍 氦气产业链上中下游</h3>
                <div class="chain-level upstream">
                    <div>
                        <strong>🔩 上游：氦气资源</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            卡塔尔(占30%产能) → 俄罗斯 → 美国 → BOG提氦(国产) → 天然气田伴生氦
                        </p>
                    </div>
                </div>
                <div class="chain-level midstream">
                    <div>
                        <strong>⚙️ 中游：提纯与储运</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            氦气提纯(林德/法液空/空气产品) → 液氦储罐 → 管束车运输 → 钢瓶/液氦杜瓦瓶
                        </p>
                    </div>
                </div>
                <div class="chain-level downstream">
                    <div>
                        <strong>🖥️ 下游：应用场景</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            半导体(光刻机/刻蚀机) → MRI医疗 → 数据中心散热 → 航天发射 → 焊接保护气
                        </p>
                    </div>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>💹 A股核心标的深度对比</h2>
            <h3 style="margin: 20px 0 15px;">🔥 第一梯队：氦气产业链</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心优势</th><th>投资信号</th></tr>
                <tr>
                    <td>中泰股份</td>
                    <td>300435</td>
                    <td>BOG提氦技术领先，LNG设备+氦气全产业链</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>杭氧股份</td>
                    <td>002430</td>
                    <td>工业气体龙头，空分设备+气体供应</td>
                    <td><span class="signal-tag buy">配置</td>
                </tr>
                <tr>
                    <td>凯美特气</td>
                    <td>002549</td>
                    <td>特种气体供应商，氦气业务布局</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
                <tr>
                    <td>华特气体</td>
                    <td>688268</td>
                    <td>电子特气龙头，6N级氦气国产化</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
            </table>
            
            <h3 style="margin: 20px 0 15px;">⚡ 第二梯队：间接受益</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心产品</th><th>投资信号</th></tr>
                <tr>
                    <td>广钢气体</td>
                    <td>688548</td>
                    <td>氦气供应，林德/法液空代理商</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
                <tr>
                    <td>和金矿业</td>
                    <td>601969</td>
                    <td>氦气勘探，天然气田伴生氦</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
            </table>
        </div>
''',
        '''
        <div class="section">
            <h2>📈 供需格局与涨价逻辑</h2>
            <table>
                <tr><th>指标</th><th>当前状态</th><th>趋势</th></tr>
                <tr><td>全球产能中断</td><td>40%</td><td class="trend-up">↑ 卡塔尔+俄罗斯断供</td></tr>
                <tr><td>库存支撑</td><td>2-4周</td><td class="trend-down">↓ 持续消耗</td></tr>
                <tr><td>交货周期</td><td>3-6个月</td><td class="trend-up">↑ 持续拉长</td></tr>
                <tr><td>价格趋势</td><td>520-560元/m³</td><td class="trend-up">↑ 年内再涨40-60%</td></tr>
                <tr><td>国产化率</td><td>快速提升</td><td class="trend-up">↑ BOG提氦突破</td></tr>
            </table>
        </div>
''',
        '''
        <div class="section">
            <h2>🎯 操作建议</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>📈 投资主线</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>核心配置：</strong>中泰股份(BOG提氦技术)、华特气体(电子特气)</li>
                        <li><strong>弹性标的：</strong>杭氧股份(工业气体龙头)</li>
                        <li><strong>潜伏标的：</strong>凯美特气(氦气布局)、广钢气体(氦气供应)</li>
                    </ul>
                </div>
                <div class="info-card">
                    <h4>⚠️ 操作策略</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>买点：</strong>回调10%后分批建仓</li>
                        <li><strong>止损：</strong>跌破买入价10%严格止损</li>
                        <li><strong>止盈：</strong>目标涨幅40-60%，分批兑现</li>
                    </ul>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>🚀 核心催化剂</h2>
            <div class="news-item">
                <span class="tag hot">供应危机</span>
                <h3>卡塔尔+俄罗斯双重断供：全球40%产能中断</h3>
                <p>卡塔尔拉斯拉凡工业城3月遭袭停产修复需3-5年；俄罗斯4月宣布氦气出口管制至2027年底。</p>
            </div>
            <div class="news-item">
                <span class="tag policy">政策</span>
                <h3>新国标GB/T4844-2025正式实施：6N级门槛提升</h3>
                <p>5月1日起新国标对6N级电子级氦气门槛全面提升，加速行业洗牌。</p>
            </div>
            <div class="news-item">
                <span class="tag hot">涨价</span>
                <h3>全球第二轮涨价生效：+26%-33%</h3>
                <p>林德、法液空、空气产品5月1日起全球提价，长协客户另加40%供应保障附加费。</p>
            </div>
            <div class="news-item">
                <span class="tag tech">国产突破</span>
                <h3>BOG提氦技术破局：成本仅为进口1/3</h3>
                <p>中国已建成12个BOG提氦项目，总产能3500万立方米/年。</p>
            </div>
        </div>
'''
    ]
    
    risk_items = [
        "地缘政治风险：国际局势缓和可能导致供应恢复",
        "替代技术风险：新型散热技术可能减少氦气需求",
        "下游需求风险：半导体行业周期性波动可能影响需求",
        "价格波动风险：氦气价格受国际局势影响大",
        "国产化不及预期：BOG提氦技术推广需要时间"
    ]
    
    short_term_items = [
        "氦气供需失衡加剧，价格高位坚挺",
        "国际巨头全面推行配给制，有价无市成常态",
        "5-8月传统旺季叠加国际提价，价格或再涨40-60%",
        "国产替代加速，BOG提氦项目产能释放"
    ]
    
    medium_term_items = [
        "全球氦气供应紧张格局延续至2027年",
        "半导体AI算力需求持续增长，氦气刚需属性强化",
        "国产替代加速，行业集中度提升",
        "新国标实施加速行业洗牌，龙头厂商受益"
    ]
    
    strategy_content = '''
                <p style="margin: 10px 0;"><strong>核心标的：</strong>中泰股份(底仓配置)+华特气体(电子特气龙头)</p>
                <p style="margin: 10px 0;"><strong>操作节奏：</strong>回调低吸为主；关注国际局势变化；严格止损</p>
                <p style="margin: 10px 0;"><strong>预期收益：</strong>氦气价格持续上涨，产业链公司业绩爆发；长期受益于国产替代</p>
    '''
    
    output_path = "./docs/reports/氦气产业链/氦气产业链标准日报.html"
    return generate_standard_report(chain_name, icon, title, date, market_data, content_sections, risk_items, short_term_items, medium_term_items, strategy_content, output_path)


def create_advanced_packaging_report():
    """生成先进封装产业链标准日报"""
    chain_name = "先进封装产业链"
    icon = "🔧"
    title = "先进封装CoWoS产业链日报 2026"
    date = "2026年5月12日"
    
    market_data = [
        {"value": ">25%", "label": "CoWoS产能缺口"},
        {"value": "+40-60%", "label": "封装价格上涨"},
        {"value": "6-9个月", "label": "交货周期"},
        {"value": "70%", "label": "英伟达产能锁定"}
    ]
    
    content_sections = [
        '''
        <div class="section">
            <h2>⚡ 产业投资逻辑</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>🔥 第一性原理</h4>
                    <p style="margin: 10px 0;"><strong>摩尔定律放缓：</strong>2.5D/3D封装成为延续算力提升的关键路径，CoWoS是AI芯片唯一解。</p>
                    <p style="margin: 10px 0;"><strong>HBM与逻辑芯片互联：</strong>CoWoS实现HBM与GPU/CPU的高带宽互联，是AI算力的核心支撑。</p>
                </div>
                <div class="info-card">
                    <h4>🎯 三大驱动逻辑</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>AI芯片需求爆发：</strong>H100/B100/GB200全面采用CoWoS封装</li>
                        <li><strong>产能扩张瓶颈：</strong>台积电CoWoS产能有限，缺口超25%</li>
                        <li><strong>国产替代空间：</strong>国内封装厂2.5D/3D产能扩张加速</li>
                    </ul>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>🗺️ 产业链全景图</h2>
            <div class="chain-diagram">
                <h3 style="color: #2E7D32; margin-bottom: 15px;">📍 先进封装产业链上中下游</h3>
                <div class="chain-level upstream">
                    <div>
                        <strong>🔩 上游：设备与材料</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            光刻机/刻蚀机(应用材料/泛林) → ABF载板(欣兴/揖斐电) → PSPI材料 → 靶材(江丰电子) → CVD/PVD设备
                        </p>
                    </div>
                </div>
                <div class="chain-level midstream">
                    <div>
                        <strong>⚙️ 中游：封装代工</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            CoWoS(台积电) → InFO(台积电) → 2.5D/3D封装(通富微电/长电科技/华天科技) → 封测代工
                        </p>
                    </div>
                </div>
                <div class="chain-level downstream">
                    <div>
                        <strong>🖥️ 下游：AI芯片</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            英伟达(H100/B100/GB200) → AMD(MI300X) → 谷歌(TPU) → 亚马逊(Trainium) → 华为(昇腾)
                        </p>
                    </div>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>💹 A股核心标的深度对比</h2>
            <h3 style="margin: 20px 0 15px;">🔥 第一梯队：封装龙头</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心优势</th><th>核心客户</th><th>投资信号</th></tr>
                <tr>
                    <td>通富微电</td>
                    <td>002156</td>
                    <td>先进封装龙头，绑定AMD，2.5D/3D封装产能</td>
                    <td>AMD、长江存储</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
                <tr>
                    <td>长电科技</td>
                    <td>600584</td>
                    <td>全球第三大封测厂，2.5D/3D封装布局</td>
                    <td>高通、华为海思</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
                <tr>
                    <td>华天科技</td>
                    <td>002185</td>
                    <td>TSV/SiP封装，先进封装占比30%</td>
                    <td>多家芯片厂</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
            </table>
            
            <h3 style="margin: 20px 0 15px;">⚡ 第二梯队：设备和材料</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心产品</th><th>投资信号</th></tr>
                <tr>
                    <td>芯源微</td>
                    <td>688037</td>
                    <td>涂胶显影设备，国产替代</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>深南电路</td>
                    <td>002916</td>
                    <td>ABF载板，封装基板</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>兴森科技</td>
                    <td>002436</td>
                    <td>IC载板，封装基板龙头</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
                <tr>
                    <td>华海清科</td>
                    <td>688083</td>
                    <td>CMP设备，国产替代</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
            </table>
        </div>
''',
        '''
        <div class="section">
            <h2>📈 供需格局</h2>
            <table>
                <tr><th>指标</th><th>当前状态</th><th>趋势</th></tr>
                <tr><td>CoWoS产能缺口</td><td>>25%</td><td class="trend-up">↑ 持续扩大</td></tr>
                <tr><td>封装价格涨幅</td><td>+40-60%</td><td class="trend-up">↑ 高位运行</td></tr>
                <tr><td>交货周期</td><td>6-9个月</td><td class="trend-up">↑ 继续拉长</td></tr>
                <tr><td>英伟达产能锁定</td><td>70%</td><td class="trend-up">↑ 持续</td></tr>
                <tr><td>国产化率</td><td><15%</td><td class="trend-up">↑ 快速提升</td></tr>
            </table>
        </div>
''',
        '''
        <div class="section">
            <h2>🎯 操作建议</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>📈 投资主线</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>核心配置：</strong>通富微电(先进封装龙头)、长电科技(封测龙头)</li>
                        <li><strong>弹性标的：</strong>芯源微(设备国产替代)、深南电路(载板)</li>
                        <li><strong>潜伏标的：</strong>华海清科(CMP设备)、兴森科技(IC载板)</li>
                    </ul>
                </div>
                <div class="info-card">
                    <h4>⚠️ 操作策略</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>买点：</strong>回调8-10%后分批建仓</li>
                        <li><strong>止损：</strong>跌破买入价8%严格止损</li>
                        <li><strong>止盈：</strong>目标涨幅30-50%，分批兑现</li>
                    </ul>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>🚀 核心催化剂</h2>
            <div class="news-item">
                <span class="tag hot">产能缺口</span>
                <h3>2026Q1全球CoWoS产能缺口超25%</h3>
                <p>封装价格上涨40-60%，交货周期拉长至6-9个月。</p>
            </div>
            <div class="news-item">
                <span class="tag hot">大客户锁定</span>
                <h3>英伟达锁定台积电70% CoWoS产能</h3>
                <p>H100/B100/GB200全面采用CoWoS封装。</p>
            </div>
            <div class="news-item">
                <span class="tag tech">技术突破</span>
                <h3>国产封装厂2.5D/3D产能扩张加速</h3>
                <p>通富微电、长电科技先进封装产能持续释放。</p>
            </div>
            <div class="news-item">
                <span class="tag policy">政策支持</span>
                <h3>大基金持续支持封装企业扩产</h3>
                <p>先进封装被列为重点突破方向，02专项支持。</p>
            </div>
        </div>
'''
    ]
    
    risk_items = [
        "设备风险：先进封装设备依赖进口，国产化率低",
        "材料风险：ABF载板、PSPI等关键材料被海外垄断",
        "竞争风险：台积电等海外厂商竞争压力",
        "需求风险：AI芯片需求周期性波动",
        "地缘风险：海外设备出口管制影响扩产"
    ]
    
    short_term_items = [
        "CoWoS供需缺口持续，封装价格高位运行",
        "通富微电、长电科技等核心标的业绩兑现",
        "AI芯片大厂(英伟达/AMD/谷歌)持续释放订单",
        "国产封装产能逐步释放，国产化率提升"
    ]
    
    medium_term_items = [
        "AI GPU全面上量，CoWoS封装需求持续爆发",
        "先进封装从可选变必选，技术壁垒持续提升",
        "国产替代加速，通富微电等深度绑定大客户",
        "封测行业集中度提升，龙头厂商受益"
    ]
    
    strategy_content = '''
                <p style="margin: 10px 0;"><strong>核心标的：</strong>通富微电(底仓配置)+长电科技(封测龙头)</p>
                <p style="margin: 10px 0;"><strong>操作节奏：</strong>回调低吸为主；关注大客户订单释放；严格止损</p>
                <p style="margin: 10px 0;"><strong>预期收益：</strong>龙头标的2026年上涨30-50%；业绩兑现期迎主升浪</p>
    '''
    
    output_path = "./docs/reports/先进封装日报/先进封装产业链标准日报.html"
    return generate_standard_report(chain_name, icon, title, date, market_data, content_sections, risk_items, short_term_items, medium_term_items, strategy_content, output_path)


def create_suan_dian_report():
    """生成算电协同产业链标准日报"""
    chain_name = "算电协同产业链"
    icon = "⚡"
    title = "算电协同产业链日报 2026"
    date = "2026年5月12日"
    
    market_data = [
        {"value": "≥80%", "label": "新建算力中心绿电占比"},
        {"value": "30%+", "label": "AI算力成本降低"},
        {"value": "5.4万P", "label": "全国总算力规模"},
        {"value": "≤1.2", "label": "数据中心PUE要求"}
    ]
    
    content_sections = [
        '''
        <div class="section">
            <h2>⚡ 产业投资逻辑</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>🔥 第一性原理</h4>
                    <p style="margin: 10px 0;"><strong>能源瓶颈：</strong>AI算力爆发导致电力需求激增，绿电配套成为刚性约束。</p>
                    <p style="margin: 10px 0;"><strong>政策倒逼：</strong>四部门联合发文，新建算力中心清洁能源占比≥80%。</p>
                </div>
                <div class="info-card">
                    <h4>🎯 三大驱动逻辑</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>政策强制落地：</strong>四部门《人工智能与能源双向赋能行动方案》</li>
                        <li><strong>示范项目投运：</strong>大唐中卫云基地绿电直供项目正式投运</li>
                        <li><strong>地方政策跟进：</strong>四川省发布算电融合发展实施意见</li>
                    </ul>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>🗺️ 产业链全景图</h2>
            <div class="chain-diagram">
                <h3 style="color: #2E7D32; margin-bottom: 15px;">📍 算电协同产业链上中下游</h3>
                <div class="chain-level upstream">
                    <div>
                        <strong>🔩 上游：清洁能源</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            光伏(隆基绿能/通威股份) → 风电(金风科技/明阳智能) → 储能(宁德时代/阳光电源) → 绿电交易
                        </p>
                    </div>
                </div>
                <div class="chain-level midstream">
                    <div>
                        <strong>⚙️ 中游：算力基础设施</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            数据中心(万国数据/秦淮数据) → 算力租赁(中科曙光/浪潮信息) → 液冷散热(英维克/高澜股份) → 电力设备
                        </p>
                    </div>
                </div>
                <div class="chain-level downstream">
                    <div>
                        <strong>🖥️ 下游：算力需求方</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            阿里/腾讯/字节/百度 → AI训练推理 → 大模型 → 行业应用
                        </p>
                    </div>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>💹 A股核心标的深度对比</h2>
            <h3 style="margin: 20px 0 15px;">🔥 第一梯队：一体化龙头</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心优势</th><th>核心客户</th><th>投资信号</th></tr>
                <tr>
                    <td>中国能建</td>
                    <td>601868</td>
                    <td>能源顶层规划独特竞争力，深度参与算力枢纽建设</td>
                    <td>国家电网、算力中心</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>中国电建</td>
                    <td>601669</td>
                    <td>新能源规划设计、储能及综合能源服务全产业链</td>
                    <td>各大能源集团</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
                <tr>
                    <td>大唐发电</td>
                    <td>601991</td>
                    <td>电力央企，绿电保供核心受益</td>
                    <td>算力中心</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
            </table>
            
            <h3 style="margin: 20px 0 15px;">⚡ 第二梯队：算力基础设施</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心产品</th><th>投资信号</th></tr>
                <tr>
                    <td>中科曙光</td>
                    <td>603019</td>
                    <td>算力租赁+液冷散热</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>英维克</td>
                    <td>002837</td>
                    <td>液冷温控龙头</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
                <tr>
                    <td>中天科技</td>
                    <td>600522</td>
                    <td>光纤涨价+算力基建+储能三重利好</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
            </table>
        </div>
''',
        '''
        <div class="section">
            <h2>🎯 操作建议</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>📈 投资主线</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>核心配置：</strong>中国能建(一体化龙头)、中国电建(PB低位)</li>
                        <li><strong>弹性标的：</strong>大唐发电(绿电保供)、中科曙光(算力+液冷)</li>
                        <li><strong>潜伏标的：</strong>英维克(液冷龙头)、中天科技(光纤+算力)</li>
                    </ul>
                </div>
                <div class="info-card">
                    <h4>⚠️ 操作策略</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>买点：</strong>回调5-10%后分批建仓</li>
                        <li><strong>止损：</strong>跌破买入价8%严格止损</li>
                        <li><strong>止盈：</strong>目标涨幅25-40%，分批兑现</li>
                    </ul>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>🚀 核心催化剂</h2>
            <div class="news-item">
                <span class="tag policy">政策重磅</span>
                <h3>四部门联合发布《人工智能与能源双向赋能行动方案》</h3>
                <p>新建算力中心清洁能源占比≥80%，配套储能设施，降低算力用电成本30%以上。</p>
            </div>
            <div class="news-item">
                <span class="tag hot">里程碑</span>
                <h3>全国首个大规模算电协同绿电直供项目投运</h3>
                <p>大唐中卫云基地50万千瓦光伏电站投运，"沙漠风光电直连数字算力"。</p>
            </div>
            <div class="news-item">
                <span class="tag policy">地方政策</span>
                <h3>四川省发布算电融合发展实施意见</h3>
                <p>在阿坝、甘孜、凉山等地建设"绿电+算力"融合发展项目。</p>
            </div>
        </div>
'''
    ]
    
    risk_items = [
        "政策落地进度不及预期：算力建设周期较长，短期业绩波动",
        "行业竞争加剧：电力市场改革带来竞争加剧",
        "消纳问题：绿电消纳存在不确定性",
        "市场情绪波动：短期涨幅过大可能调整",
        "盈利能力风险：电力央企收益率较低"
    ]
    
    short_term_items = [
        "四部门政策催化，算电协同主题活跃",
        "大唐发电、中科曙光等核心标的持续表现",
        "绿电直供示范项目持续落地",
        "电力央企估值修复空间大"
    ]
    
    medium_term_items = [
        "政策强制落地，新建算力中心必须配套绿电",
        "绿电占比80%+，算力运营成本降低30%以上",
        "全国总算力规模持续扩张，电力需求激增",
        "电力央企深度参与算力枢纽建设，订单释放"
    ]
    
    strategy_content = '''
                <p style="margin: 10px 0;"><strong>核心标的：</strong>中国能建(底仓配置)+大唐发电(绿电保供)</p>
                <p style="margin: 10px 0;"><strong>操作节奏：</strong>回调低吸为主；关注政策落地进度；严格止损</p>
                <p style="margin: 10px 0;"><strong>预期收益：</strong>电力央企估值修复+算力订单释放，2026年上涨20-40%</p>
    '''
    
    output_path = "./docs/reports/算电协同产业链/算电协同产业链标准日报.html"
    return generate_standard_report(chain_name, icon, title, date, market_data, content_sections, risk_items, short_term_items, medium_term_items, strategy_content, output_path)


def main():
    """主函数，批量生成所有产业链标准日报"""
    print("=" * 60)
    print("🚀 开始生成统一格式的产业链日报...")
    print("=" * 60)
    
    reports = [
        ("CPO产业链", create_cpo_report),
        ("存储产业链", create_storage_report),
        ("商业航天产业链", create_commercial_space_report),
        ("铜箔产业链", create_copper_foil_report),
        ("氦气产业链", create_helium_report),
        ("先进封装产业链", create_advanced_packaging_report),
        ("算电协同产业链", create_suan_dian_report),
    ]
    
    for name, func in reports:
        print(f"\n📝 生成 {name} 标准日报...")
        try:
            func()
        except Exception as e:
            print(f"❌ {name} 生成失败: {e}")
    
    print("\n" + "=" * 60)
    print("✅ 所有产业链日报生成完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
