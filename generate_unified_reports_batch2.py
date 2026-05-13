#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一产业链日报格式生成器 - 第二批
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
        .signal-tag {{ display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 0.8em; margin-left: 5px; }}
        .signal-tag.buy {{ background: #4CAF50; color: white; }}
        .signal-tag.sell {{ background: #ef4444; color: white; }}
        .signal-tag.hold {{ background: #ffc107; color: white; }}
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


def create_embodied_ai_report():
    """生成具身智能产业链标准日报"""
    chain_name = "具身智能机器人产业链"
    icon = "🤖"
    title = "具身智能机器人产业链日报 2026"
    date = "2026年5月12日"
    
    market_data = [
        {"value": "380亿元", "label": "2026年市场规模(+168%)"},
        {"value": "850亿元", "label": "2027年预测市场规模"},
        {"value": "65%", "label": "减速器国产化率"},
        {"value": "1万台", "label": "Optimus 2026年目标"}
    ]
    
    content_sections = [
        '''
        <div class="section">
            <h2>⚡ 产业投资逻辑</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>🔥 第一性原理</h4>
                    <p style="margin: 10px 0;"><strong>具身智能是AI终极形态：</strong>大模型赋能机器人实现感知、认知、决策一体化，人形机器人是终极载体。</p>
                    <p style="margin: 10px 0;"><strong>政策强力支持：</strong>政府工作报告首次列入具身智能，与集成电路、航空航天并列。</p>
                </div>
                <div class="info-card">
                    <h4>🎯 三大驱动逻辑</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>AI大模型突破：</strong>具身智能大模型能力持续提升，泛化能力增强</li>
                        <li><strong>量产元年到来：</strong>2026年被定义为"具身智能量产元年"</li>
                        <li><strong>国产替代加速：</strong>减速器、伺服电机等核心零部件国产化率提升</li>
                    </ul>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>🗺️ 产业链全景图</h2>
            <div class="chain-diagram">
                <h3 style="color: #2E7D32; margin-bottom: 15px;">📍 具身智能产业链上中下游</h3>
                <div class="chain-level upstream">
                    <div>
                        <strong>🔩 上游：核心零部件</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            减速器(绿的谐波/中大力德) → 伺服电机(鸣志电器/汇川技术) → 控制器(汇川技术) → 力传感器(柯力传感) → 丝杠(贝斯特)
                        </p>
                    </div>
                </div>
                <div class="chain-level midstream">
                    <div>
                        <strong>⚙️ 中游：整机集成</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            人形机器人(宇树/智元/傅利叶) → 四足机器人 → 机械臂 → AI大脑(华为盘古)
                        </p>
                    </div>
                </div>
                <div class="chain-level downstream">
                    <div>
                        <strong>🖥️ 下游：应用场景</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            工业制造 → 仓储物流 → 商业服务 → 家庭陪伴 → 特种作业
                        </p>
                    </div>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>💹 A股核心标的深度对比</h2>
            <h3 style="margin: 20px 0 15px;">🔥 第一梯队：核心零部件</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心优势</th><th>核心客户</th><th>投资信号</th></tr>
                <tr>
                    <td>绿的谐波</td>
                    <td>688017</td>
                    <td>谐波减速器龙头，国产替代，人形机器人批量配套</td>
                    <td>宇树、智元、特斯拉</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
                <tr>
                    <td>中大力德</td>
                    <td>002896</td>
                    <td>RV减速器+谐波减速器双布局</td>
                    <td>多家机器人厂商</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>汇川技术</td>
                    <td>300124</td>
                    <td>伺服电机+控制器龙头</td>
                    <td>工业自动化</td>
                    <td><span class="signal-tag buy">持有</span></td>
                </tr>
            </table>
            
            <h3 style="margin: 20px 0 15px;">⚡ 第二梯队：传感器与丝杠</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心产品</th><th>投资信号</th></tr>
                <tr>
                    <td>鸣志电器</td>
                    <td>603728</td>
                    <td>步进电机龙头，切入机器人赛道</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>柯力传感</td>
                    <td>603662</td>
                    <td>力传感器，机器人传感器布局</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
                <tr>
                    <td>贝斯特</td>
                    <td>300580</td>
                    <td>丝杠、滚珠丝杠副</td>
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
                        <li><strong>核心配置：</strong>绿的谐波(谐波减速器龙头)、中大力德(RV+谐波双布局)</li>
                        <li><strong>弹性标的：</strong>鸣志电器(电机切入机器人)、贝斯特(丝杠国产替代)</li>
                        <li><strong>潜伏标的：</strong>柯力传感(力传感器)、汇川技术(伺服+控制器)</li>
                    </ul>
                </div>
                <div class="info-card">
                    <h4>⚠️ 操作策略</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>买点：</strong>回调10-15%后分批建仓</li>
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
                <span class="tag policy">政策催化</span>
                <h3>政府工作报告首次列入具身智能</h3>
                <p>与集成电路、航空航天并列，多地设立产业基金总规模超500亿元。</p>
            </div>
            <div class="news-item">
                <span class="tag hot">量产催化</span>
                <h3>2026年被定义为"具身智能量产元年"</h3>
                <p>宇树科技人形机器人H1全球出货量第一，特斯拉Optimus目标量产1万台。</p>
            </div>
            <div class="news-item">
                <span class="tag tech">技术突破</span>
                <h3>华为盘古具身智能大模型发布</h3>
                <p>具身智能大模型能力持续提升，泛化能力增强。</p>
            </div>
            <div class="news-item">
                <span class="tag">补贴政策</span>
                <h3>人形机器人采购补贴政策即将出台</h3>
                <p>最高补贴30%，北京、上海、深圳率先开展应用试点。</p>
            </div>
        </div>
'''
    ]
    
    risk_items = [
        "技术路线不确定性：人形机器人技术仍在验证期，成本居高不下",
        "量产进度不及预期：核心零部件产能制约整机量产",
        "竞争加剧风险：国内外企业加速布局，竞争格局未定",
        "商业化落地慢：应用场景仍需开拓，短期难以大规模商业化",
        "估值过高风险：部分标的估值偏高，需等待业绩兑现"
    ]
    
    short_term_items = [
        "政策持续催化，具身智能主题活跃",
        "绿的谐波、中大力德等核心标的持续表现",
        "人形机器人量产进展持续催化",
        "华为、特斯拉等巨头动态持续扰动板块"
    ]
    
    medium_term_items = [
        "2026年量产元年，产业链进入业绩兑现期",
        "核心零部件国产化加速，减速器、伺服电机等订单释放",
        "人形机器人应用场景持续开拓",
        "政府补贴政策出台加速商业化落地"
    ]
    
    strategy_content = '''
                <p style="margin: 10px 0;"><strong>核心标的：</strong>绿的谐波(底仓配置)+中大力德(弹性进攻)</p>
                <p style="margin: 10px 0;"><strong>操作节奏：</strong>回调低吸为主；关注量产进度；严格止损</p>
                <p style="margin: 10px 0;"><strong>预期收益：</strong>龙头标的2026年上涨50-100%；量产兑现后迎主升浪</p>
    '''
    
    output_path = "./docs/reports/具身智能日报/具身智能产业链标准日报.html"
    return generate_standard_report(chain_name, icon, title, date, market_data, content_sections, risk_items, short_term_items, medium_term_items, strategy_content, output_path)


def create_ai_glasses_report():
    """生成AI眼镜产业链标准日报"""
    chain_name = "AI眼镜产业链"
    icon = "👓"
    title = "AI眼镜产业链日报 2026"
    date = "2026年5月12日"
    
    market_data = [
        {"value": "Meta Ray-Ban", "label": "全球销量破千万副"},
        {"value": "500元", "label": "AI眼镜入门价格"},
        {"value": "1亿+", "label": "2026年预测出货量"},
        {"value": "300%", "label": "行业年增速"}
    ]
    
    content_sections = [
        '''
        <div class="section">
            <h2>⚡ 产业投资逻辑</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>🔥 第一性原理</h4>
                    <p style="margin: 10px 0;"><strong>AI+眼镜=下一代计算平台：</strong>Meta Ray-Ban成功验证轻量级AI眼镜市场，空间计算成为趋势。</p>
                    <p style="margin: 10px 0;"><strong>巨头全面布局：</strong>Meta、苹果、谷歌、华为、小米、三星均加速AI眼镜研发。</p>
                </div>
                <div class="info-card">
                    <h4>🎯 三大驱动逻辑</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>爆款产品验证：</strong>Meta Ray-Ban销量破千万，证明市场需求</li>
                        <li><strong>AI大模型赋能：</strong>多模态AI提升眼镜智能化体验</li>
                        <li><strong>成本持续下降：</strong>入门级AI眼镜价格下探至500元以内</li>
                    </ul>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>🗺️ 产业链全景图</h2>
            <div class="chain-diagram">
                <h3 style="color: #2E7D32; margin-bottom: 15px;">📍 AI眼镜产业链上中下游</h3>
                <div class="chain-level upstream">
                    <div>
                        <strong>🔩 上游：核心零部件</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            芯片(高通/联发科) → 摄像头(舜宇光学) → 镜片(康宁/蔡司) → 电池(亿纬锂能) → PCB/FPC → 扬声器/麦克风
                        </p>
                    </div>
                </div>
                <div class="chain-level midstream">
                    <div>
                        <strong>⚙️ 中游：整机制造</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            Meta/苹果/华为/小米/三星 → 歌尔股份(代工) → 博士眼镜(渠道) → 雷柏科技(配件)
                        </p>
                    </div>
                </div>
                <div class="chain-level downstream">
                    <div>
                        <strong>🖥️ 下游：应用场景</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            社交媒体 → 导航指引 → 翻译 → AI助手 → 拍摄记录 → 电商购物
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
                    <td>歌尔股份</td>
                    <td>002241</td>
                    <td>AR/VR代工龙头，Meta/苹果核心供应商</td>
                    <td>Meta、苹果、索尼</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
                <tr>
                    <td>舜宇光学</td>
                    <td>2382.HK</td>
                    <td>摄像头模组全球领先，AR光学核心</td>
                    <td>Meta、苹果、华为</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>亿纬锂能</td>
                    <td>300014</td>
                    <td>微型电池，AR眼镜核心供应商</td>
                    <td>Meta、三星</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
            </table>
            
            <h3 style="margin: 20px 0 15px;">⚡ 第二梯队：配套企业</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心产品</th><th>投资信号</th></tr>
                <tr>
                    <td>博士眼镜</td>
                    <td>603622</td>
                    <td>眼镜连锁，AI眼镜渠道</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
                <tr>
                    <td>立讯精密</td>
                    <td>002475</td>
                    <td>精密制造，AR/VR布局</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>欣旺达</td>
                    <td>300207</td>
                    <td>消费电子电池</td>
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
                        <li><strong>核心配置：</strong>歌尔股份(AR/VR代工龙头)</li>
                        <li><strong>弹性标的：</strong>舜宇光学(摄像头模组)、亿纬锂能(微型电池)</li>
                        <li><strong>潜伏标的：</strong>立讯精密(精密制造)、博士眼镜(渠道)</li>
                    </ul>
                </div>
                <div class="info-card">
                    <h4>⚠️ 操作策略</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>买点：</strong>回调10%后分批建仓</li>
                        <li><strong>止损：</strong>跌破买入价10%严格止损</li>
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
                <span class="tag hot">爆款催化</span>
                <h3>Meta Ray-Ban全球销量破千万副</h3>
                <p>验证轻量级AI眼镜市场需求，Meta追加订单。</p>
            </div>
            <div class="news-item">
                <span class="tag hot">新品催化</span>
                <h3>苹果/华为/小米AI眼镜新品发布</h3>
                <p>各大厂商加速AI眼镜研发，新品密集发布期临近。</p>
            </div>
            <div class="news-item">
                <span class="tag tech">技术突破</span>
                <h3>AI大模型赋能眼镜智能化</h3>
                <p>多模态AI提升眼镜交互体验，空间计算成为趋势。</p>
            </div>
            <div class="news-item">
                <span class="tag">成本下降</span>
                <h3>AI眼镜入门价格下探至500元</h3>
                <p>成本持续下降，渗透率加速提升。</p>
            </div>
        </div>
'''
    ]
    
    risk_items = [
        "产品体验不及预期：消费者对AI眼镜接受度存在不确定性",
        "技术瓶颈：续航、发热、重量等问题制约发展",
        "竞争加剧：国内外企业加速布局，竞争格局未定",
        "应用场景有限：当前AI功能相对基础，用户粘性不高",
        "估值过高风险：部分标的估值偏高"
    ]
    
    short_term_items = [
        "Meta Ray-Ban销量持续超预期，催化板块",
        "歌尔股份、舜宇光学等核心标的持续表现",
        "各大厂商AI眼镜新品发布催化板块",
        "AI大模型迭代提升产品力预期"
    ]
    
    medium_term_items = [
        "AI眼镜渗透率加速提升，行业进入高速增长期",
        "苹果、华为等巨头产品发布，带动产业链爆发",
        "核心零部件国产化加速，代工订单释放",
        "应用场景持续开拓，用户粘性提升"
    ]
    
    strategy_content = '''
                <p style="margin: 10px 0;"><strong>核心标的：</strong>歌尔股份(底仓配置)+舜宇光学(光学龙头)</p>
                <p style="margin: 10px 0;"><strong>操作节奏：</strong>回调低吸为主；关注新品发布；严格止损</p>
                <p style="margin: 10px 0;"><strong>预期收益：</strong>龙头标的2026年上涨30-50%；新品发布催化短期行情</p>
    '''
    
    output_path = "./docs/reports/AI眼镜日报/AI眼镜产业链标准日报.html"
    return generate_standard_report(chain_name, icon, title, date, market_data, content_sections, risk_items, short_term_items, medium_term_items, strategy_content, output_path)


def create_evtol_report():
    """生成eVTOL产业链标准日报"""
    chain_name = "eVTOL产业链"
    icon = "✈️"
    title = "eVTOL产业链日报 2026"
    date = "2026年5月12日"
    
    market_data = [
        {"value": "2万亿元", "label": "2030年全球eVTOL市场规模"},
        {"value": "2026", "label": "适航证颁发元年"},
        {"value": "100+城市", "label": "国内UAM规划城市"},
        {"value": "500亿+", "label": "国内产业基金规模"}
    ]
    
    content_sections = [
        '''
        <div class="section">
            <h2>⚡ 产业投资逻辑</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>🔥 第一性原理</h4>
                    <p style="margin: 10px 0;"><strong>城市空中出行革命：</strong>eVTOL将重构城市交通，实现"空中Uber"愿景。</p>
                    <p style="margin: 10px 0;"><strong>政策强力支持：</strong>民航局发布适航认证规范，2026年成为适航证颁发元年。</p>
                </div>
                <div class="info-card">
                    <h4>🎯 三大驱动逻辑</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>适航认证加速：</strong>峰飞航空等企业获型号合格证，商业化落地</li>
                        <li><strong>巨头全面布局：</strong>小鹏汇天、亿航智能、歌尔航空进展加速</li>
                        <li><strong>城市UAM规划：</strong>100+城市启动城市空中交通规划</li>
                    </ul>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>🗺️ 产业链全景图</h2>
            <div class="chain-diagram">
                <h3 style="color: #2E7D32; margin-bottom: 15px;">📍 eVTOL产业链上中下游</h3>
                <div class="chain-level upstream">
                    <div>
                        <strong>🔩 上游：核心零部件</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            电机/电调(卧龙电驱) → 电池(宁德时代/亿纬锂能) → 复合材料(中航高科) → 飞控系统 → 导航系统
                        </p>
                    </div>
                </div>
                <div class="chain-level midstream">
                    <div>
                        <strong>⚙️ 中游：整机与系统</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            整机(小鹏汇天/亿航智能/峰飞航空) → 运营商 → 低空管理 → 停机坪建设
                        </p>
                    </div>
                </div>
                <div class="chain-level downstream">
                    <div>
                        <strong>🖥️ 下游：应用场景</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            城市空中出行 → 景区旅游 → 医疗急救 → 物流配送 → 农业植保
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
                    <td>亿航智能</td>
                    <td>EH.US</td>
                    <td>全球首家上市eVTOL企业，适航认证领先</td>
                    <td>全球多国政府</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>卧龙电驱</td>
                    <td>600580</td>
                    <td>电机/电调龙头，eVTOL核心供应商</td>
                    <td>小鹏汇天等</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>宁德时代</td>
                    <td>300750</td>
                    <td>凝聚态电池，eVTOL电池核心供应商</td>
                    <td>多家eVTOL厂商</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
            </table>
            
            <h3 style="margin: 20px 0 15px;">⚡ 第二梯队：配套企业</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心产品</th><th>投资信号</th></tr>
                <tr>
                    <td>中航高科</td>
                    <td>600862</td>
                    <td>碳纤维复合材料</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>亿纬锂能</td>
                    <td>300014</td>
                    <td>新型电池，eVTOL布局</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
                <tr>
                    <td>航天宏图</td>
                    <td>688066</td>
                    <td>低空管理，UAM基础设施</td>
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
                        <li><strong>核心配置：</strong>卧龙电驱(电机龙头)、亿航智能(EH美股)</li>
                        <li><strong>弹性标的：</strong>宁德时代(凝聚态电池)、中航高科(复合材料)</li>
                        <li><strong>潜伏标的：</strong>亿纬锂能(新型电池)、航天宏图(UAM基础设施)</li>
                    </ul>
                </div>
                <div class="info-card">
                    <h4>⚠️ 操作策略</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>买点：</strong>回调15%后分批建仓</li>
                        <li><strong>止损：</strong>跌破买入价12%严格止损</li>
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
                <span class="tag policy">适航认证</span>
                <h3>峰飞航空获型号合格证</h3>
                <p>2026年成为eVTOL适航证颁发元年，商业化落地加速。</p>
            </div>
            <div class="news-item">
                <span class="tag hot">政策催化</span>
                <h3>100+城市启动UAM规划</h3>
                <p>国内城市空中交通规划密集出台，低空经济纳入国家战略。</p>
            </div>
            <div class="news-item">
                <span class="tag hot">产业基金</span>
                <h3>国内eVTOL产业基金规模超500亿</h3>
                <p>资本加速涌入，支撑产业链发展。</p>
            </div>
            <div class="news-item">
                <span class="tag tech">技术突破</span>
                <h3>宁德时代凝聚态电池量产</h3>
                <p>eVTOL电池能量密度突破，续航里程提升。</p>
            </div>
        </div>
'''
    ]
    
    risk_items = [
        "适航认证进度不及预期：安全标准严格，认证周期较长",
        "商业化落地慢：城市空中出行基础设施不完善",
        "安全事故风险：eVTOL安全性要求极高，事故影响大",
        "政策支持不及预期：低空开放进度可能低于预期",
        "估值过高风险：部分标的处于早期阶段，估值偏高"
    ]
    
    short_term_items = [
        "适航认证消息持续催化板块",
        "峰飞航空、小鹏汇天等新品发布催化",
        "城市UAM规划密集出台",
        "产业资本持续涌入"
    ]
    
    medium_term_items = [
        "2026年适航证颁发元年，商业化加速",
        "国内eVTOL订单持续释放，产业链进入业绩兑现期",
        "低空经济纳入国家战略，政策持续支持",
        "电池、电机等核心零部件订单爆发"
    ]
    
    strategy_content = '''
                <p style="margin: 10px 0;"><strong>核心标的：</strong>卧龙电驱(底仓配置)+亿航智能(EH美股弹性)</p>
                <p style="margin: 10px 0;"><strong>操作节奏：</strong>回调低吸为主；关注适航认证进展；严格止损</p>
                <p style="margin: 10px 0;"><strong>预期收益：</strong>龙头标的2026年上涨50-100%；商业化兑现后迎主升浪</p>
    '''
    
    output_path = "./docs/reports/eVTOL日报/eVTOL产业链标准日报.html"
    return generate_standard_report(chain_name, icon, title, date, market_data, content_sections, risk_items, short_term_items, medium_term_items, strategy_content, output_path)


def create_pcb_report():
    """生成PCB产业链标准日报"""
    chain_name = "PCB产业链"
    icon = "🔲"
    title = "PCB产业链日报 2026"
    date = "2026年5月12日"
    
    market_data = [
        {"value": "7-7.5元/米", "label": "7628电子布(+150%)"},
        {"value": "200-220元/张", "label": "FR-4覆铜板(+100%)"},
        {"value": "42-45万元/吨", "label": "HVLP铜箔(+50%)"},
        {"value": "48%", "label": "电子布供需缺口"}
    ]
    
    content_sections = [
        '''
        <div class="section">
            <h2>⚡ 产业投资逻辑</h2>
            <div class="info-grid">
                <div class="info-card">
                    <h4>🔥 第一性原理</h4>
                    <p style="margin: 10px 0;"><strong>AI服务器PCB价值量3-5倍：</strong>AI服务器PCB层数从10层→20-30层，材料升级带动价值量暴增。</p>
                    <p style="margin: 10px 0;"><strong>四大材料全线涨价：</strong>电子布+150%、覆铜板+100%、铜箔+50%、树脂+24%。</p>
                </div>
                <div class="info-card">
                    <h4>🎯 三大驱动逻辑</h4>
                    <ul style="margin-left: 20px;">
                        <li><strong>AI服务器需求爆发：</strong>GB200/H200带动高端PCB需求激增</li>
                        <li><strong>供需缺口持续：</strong>电子布月缺口800-900万米，HVLP缺口48%</li>
                        <li><strong>扩产周期长：</strong>电子布产能最早9-10月释放</li>
                    </ul>
                </div>
            </div>
        </div>
''',
        '''
        <div class="section">
            <h2>🗺️ 产业链全景图</h2>
            <div class="chain-diagram">
                <h3 style="color: #2E7D32; margin-bottom: 15px;">📍 PCB产业链上中下游</h3>
                <div class="chain-level upstream">
                    <div>
                        <strong>🔩 上游：原材料</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            铜箔(诺德股份) → 电子布(宏和科技/中国巨石) → 环氧树脂(万华化学) → PPE树脂
                        </p>
                    </div>
                </div>
                <div class="chain-level midstream">
                    <div>
                        <strong>⚙️ 中游：覆铜板与PCB</strong>
                        <p style="margin: 5px 0; font-size: 0.9em;">
                            覆铜板(生益科技/南亚新材/华正新材) → PCB(鹏鼎控股/东山精密) → IC载板
                        </p>
                    </div>
                </div>
                <div class="chain-level downstream">
                    <div>
                        <strong>🖥️ 下游：应用场景</strong>
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
                <tr><th>公司</th><th>股票代码</th><th>核心优势</th><th>Q1净利增速</th><th>投资信号</th></tr>
                <tr>
                    <td>生益科技</td>
                    <td>600183</td>
                    <td>覆铜板份额全球第二，高端产品占比提升</td>
                    <td>+91.76%</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
                <tr>
                    <td>南亚新材</td>
                    <td>688519</td>
                    <td>覆铜板核心标的，持续创新高</td>
                    <td>+377.6%</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
                <tr>
                    <td>金安国纪</td>
                    <td>002636</td>
                    <td>覆铜板弹性标的</td>
                    <td>+655-871%</td>
                    <td><span class="signal-tag buy">强势</span></td>
                </tr>
                <tr>
                    <td>华正新材</td>
                    <td>603186</td>
                    <td>高端覆铜板产能扩张</td>
                    <td>扭亏为盈</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
            </table>
            
            <h3 style="margin: 20px 0 15px;">⚡ 第二梯队：原材料与PCB</h3>
            <table>
                <tr><th>公司</th><th>股票代码</th><th>核心产品</th><th>投资信号</th></tr>
                <tr>
                    <td>宏和科技</td>
                    <td>603256</td>
                    <td>电子布龙头，最直接受益</td>
                    <td><span class="signal-tag buy">配置</span></td>
                </tr>
                <tr>
                    <td>中国巨石</td>
                    <td>600176</td>
                    <td>10万吨电子布扩产</td>
                    <td><span class="signal-tag hold">持有</span></td>
                </tr>
                <tr>
                    <td>鹏鼎控股</td>
                    <td>002938</td>
                    <td>PCB全球第一，苹果核心</td>
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
                        <li><strong>核心配置：</strong>生益科技(覆铜板龙头)、南亚新材(持续新高)</li>
                        <li><strong>弹性标的：</strong>金安国纪(Q1业绩+655-871%)、宏和科技(电子布)</li>
                        <li><strong>潜伏标的：</strong>华正新材(高端产能扩张)、鹏鼎控股(PCB份额第一)</li>
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
                <h3>四大材料全线涨价：电子布+150%、覆铜板+100%</h3>
                <p>建滔积层板再发涨价函，5月FR-4系列覆铜板全面上调10%。</p>
            </div>
            <div class="news-item">
                <span class="tag hot">供需紧张</span>
                <h3>电子布月缺口800-900万米，HVLP缺口48%</h3>
                <p>CCL库存仅10%，客户交期从7-10天拉长至15-25天+。</p>
            </div>
            <div class="news-item">
                <span class="tag tech">扩产</span>
                <h3>中国巨石10万吨电子布首批4月已落地</h3>
                <p>剩余5万吨预计8-9月，产能释放仍需时间。</p>
            </div>
            <div class="news-item">
                <span class="tag policy">传导</span>
                <h3>提价已实现对上游成本超额覆盖</h3>
                <p>CCL每次提价幅度10%以上，覆盖上游成本涨幅。</p>
            </div>
        </div>
'''
    ]
    
    risk_items = [
        "铜价波动风险：铜价受宏观经济影响大，可能回调",
        "产能扩张过快：多家企业扩产可能导致供需逆转",
        "技术替代风险：新材料可能替代传统材料",
        "下游需求不及预期：AI服务器出货量可能低于预期",
        "短期涨幅过大：部分个股乖离率偏高"
    ]
    
    short_term_items = [
        "PCB板块强势不改，生益科技、南亚新材等持续创新高",
        "四大材料涨价持续，成本推动逻辑延续",
        "电子布、HVLP铜箔供需缺口持续，涨价趋势明确",
        "覆铜板Q1业绩爆发，业绩兑现期关注超预期标的"
    ]
    
    medium_term_items = [
        "AI服务器PCB价值量是普通服务器3-5倍，需求持续爆发",
        "电子布月缺口800-900万米，涨价趋势延续至2027年",
        "覆铜板龙头量价齐升，业绩进入高速增长通道",
        "行业集中度提升，龙头厂商受益于供给侧改革"
    ]
    
    strategy_content = '''
                <p style="margin: 10px 0;"><strong>核心标的：</strong>生益科技(底仓配置)+南亚新材(弹性进攻)</p>
                <p style="margin: 10px 0;"><strong>操作节奏：</strong>回调低吸为主；关注涨价动态；严格止损</p>
                <p style="margin: 10px 0;"><strong>预期收益：</strong>龙头标的2026年上涨30-50%；涨价周期延续至2027年</p>
    '''
    
    output_path = "./PCB产业链日报/PCB产业链标准日报.html"
    return generate_standard_report(chain_name, icon, title, date, market_data, content_sections, risk_items, short_term_items, medium_term_items, strategy_content, output_path)


def main():
    """主函数，批量生成所有产业链标准日报"""
    print("=" * 60)
    print("🚀 开始生成第二批统一格式的产业链日报...")
    print("=" * 60)
    
    reports = [
        ("具身智能产业链", create_embodied_ai_report),
        ("AI眼镜产业链", create_ai_glasses_report),
        ("eVTOL产业链", create_evtol_report),
        ("PCB产业链", create_pcb_report),
    ]
    
    for name, func in reports:
        print(f"\n📝 生成 {name} 标准日报...")
        try:
            func()
        except Exception as e:
            print(f"❌ {name} 生成失败: {e}")
    
    print("\n" + "=" * 60)
    print("✅ 第二批产业链日报生成完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
