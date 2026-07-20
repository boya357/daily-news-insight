#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日系统维护 - 数据更新脚本
2026-07-20
"""
import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"   ✅ 已保存: {path}")

def update_portfolio():
    print("📊 更新持仓智能预警仪表盘数据...")
    path = os.path.join(DATA_DIR, 'portfolio.json')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    current_time = data.get('update_time', '')
    portfolio_time = data.get('portfolio', {}).get('update_time', '')
    has_today = '2026年07月20日' in current_time or '2026年07月20日' in portfolio_time
    
    if has_today:
        print(f"   ℹ️  portfolio.json 已含今日数据，重新计算健康分")
        stocks = data.get('stocks', [])
        stop_loss_break = sum(1 for s in stocks if s.get('current_price', 0) < s.get('stop_loss_price', 0))
        limit_down = sum(1 for s in stocks if s.get('today_change', 0) <= -0.095)
        profit_count = sum(1 for s in stocks if s.get('current_price', 0) > s.get('cost_price', 0))
        
        health = 100 - stop_loss_break * 25 - limit_down * 15 - (len(stocks) - profit_count) * 10
        health = max(0, min(100, health))
        
        data['portfolio']['health_score'] = health
        data['portfolio']['stop_loss_break_count'] = stop_loss_break
        data['portfolio']['profit_count'] = profit_count
        data['portfolio']['loss_count'] = len(stocks) - profit_count
        
        save_json(path, data)
        return True
    else:
        print(f"   ⚠️  portfolio.json 更新时间非今日")
        return False

def update_topics():
    print("🎯 更新智能选题助手数据...")
    path = os.path.join(DATA_DIR, 'topics.json')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    data['system_info']['last_update'] = '2026-07-20'
    data['system_info']['total_topics'] = 10
    data['system_info']['s_level_count'] = 1
    data['system_info']['a_level_count'] = 1
    data['system_info']['b_level_count'] = 6
    data['system_info']['c_level_count'] = 2
    data['system_info']['update_note'] = '7/20周一市场极度割裂：权重护盘指数红（沪指+0.85%）但3700+个股下跌，科技成长股全面崩盘（半导体指数-5.61%、PCB-8.4%），267只个股跌停。S级仅剩医药防御主线，算力降为A级观察，存储/半导体设备/机器人继续下调评级，高股息红利/白酒消费成新共识防御方向。'
    
    s_topics = data.get('s_level_topics', [])
    a_topics = data.get('a_level_topics', [])
    b_topics = data.get('b_level_topics', [])
    c_topics = data.get('c_level_topics', [])
    
    new_s = []
    for t in s_topics:
        if t.get('name') == '医药生物（创新药+中药+CXO）':
            t['total_score'] = 88
            t['dimension_scores']['capital'] = 90
            t['dimension_scores']['sentiment'] = 88
            t['core_logic'] = 'S级最强防御主线：7/20市场极度割裂，沪指+0.85%但3700+个股下跌，科技股全面崩盘背景下，医药板块再度成为资金避风港。创新药权重托底创业板指，中药/医药商业延续防御强势。政策面（中医药振兴十五五规划）+基本面（创新药对外授权高增+实验猴涨价）+资金面（机构从科技切换至医药防御）三重共振。中国太保等险资明确表态将持续布局科技成长+消费+医药，长线资金支撑。'
            t['recent_performance'] = '今日创新药权重逆势走强托底创业板指，中药/医药商业继续防御属性凸显，板块相对收益显著'
            t['operation_strategy'] = 'S级防御配置：20%-25%仓位，以机构重仓的中药+CXO龙头为主，作为组合压舱石'
            t['trend'] = 'rising'
            new_s.append(t)
        elif t.get('name') == 'AI算力/云计算':
            t['level'] = 'A'
            t['total_score'] = 70
            t['core_logic'] = 'A级观察：算力网建设+8000亿特别国债长期逻辑不变，但短期科技成长股遭遇系统性估值杀跌。7/20半导体指数-5.61%、PCB板块-8.4%，科技板块从早盘+3.5%冲高到收盘-5%+，冲高跳水幅度巨大。长鑫科技上市虹吸效应+机构集中兑现+中报业绩验证压力，三重因素叠加。端侧AI/AI软件应用相对抗跌但也难独善其身。调整到位后仍是中长期配置主线，但短期需严控仓位等待企稳信号。'
            t['recent_performance'] = '今日冲高后大幅跳水，半导体指数-5.61%、PCB-8.4%，267只个股跌停，科技成长股全线重挫'
            t['risk_note'] = '科技成长股估值杀跌趋势未止，长鑫上市虹吸+机构兑现+中报压力，短期可能继续探底'
            t['operation_strategy'] = 'A级观察期：降至5%-10%仓位，优先配置端侧AI/AI软件应用等相对抗跌方向，硬件端继续减仓'
            t['trend'] = 'falling'
            a_topics.append(t)
    
    data['s_level_topics'] = new_s
    
    new_a = []
    for t in a_topics:
        if t.get('name') == '存储芯片/HBM':
            t['level'] = 'B'
            t['total_score'] = 65
            t['dimension_scores']['capital'] = 35
            t['dimension_scores']['sentiment'] = 30
            t['core_logic'] = 'B级观察（从A下调）：存储芯片超级周期长期逻辑未破，但短期遭遇毁灭性打击。7/20铜冠铜箔20cm跌停（中报增486%但环比下滑戳破高增长预期），德明利/深科技/长电科技等集体跌停，PCB板块-8.4%，半导体指数-5.61%。长鑫科技上市虹吸效应+机构集中兑现+业绩环比不及预期，三重利空叠加。HBM/DRAM涨价逻辑不变，但板块估值过高+情绪崩塌，短期需时间消化调整幅度可能达30%-40%。'
            t['recent_performance'] = ['今日板块再遭重创，铜冠铜箔20cm跌停，德明利/深科技/长电科技跌停，半导体指数-5.61%']
            t['risk_note'] = '短期恐慌性杀跌动能极强，铜冠铜箔业绩暴增却跌停说明利好出尽逻辑，板块可能继续下探20%-30%'
            t['operation_strategy'] = 'B级观察期：降至3%-5%底仓，严禁抄底，等待板块缩量企稳+情绪修复后再评估'
            t['trend'] = 'falling'
            b_topics.append(t)
        else:
            new_a.append(t)
    
    data['a_level_topics'] = new_a
    
    new_b = []
    
    dividend_topic = {
        "id": "topic_b010",
        "name": "高股息红利（油气/煤炭/电力）",
        "level": "B",
        "total_score": 75,
        "dimension_scores": {
            "policy": 80, "industry": 70, "capital": 92, "sentiment": 85,
            "valuation": 88, "catalyst": 65, "market": 90
        },
        "icon": "🏭",
        "color": "yellow",
        "core_logic": "B级最强防御方向：7/20市场极度割裂，高股息红利板块成为资金最确定的抱团方向。油气（中国海油涨停）、煤炭（中煤能源涨停）、电力（华银电力涨停）全线大涨，是全天最稳的防御抱团方向。低估值+高股息+稳现金流，在科技股估值杀跌期具备显著的防御配置价值。国家队+险资增持方向明确，中国太保等险资表态持续布局。",
        "core_stocks": ["中国海油", "中国神华", "陕西煤业", "华电能源", "中煤能源", "长江电力", "中国石油"],
        "recent_performance": "今日领涨两市，中国海油/中煤能源/华银电力等批量涨停，红利指数全线走强",
        "risk_note": "纯防御属性，上涨空间有限，市场企稳后资金可能回流成长股",
        "operation_strategy": "B级防御配置：10%-15%仓位，作为组合防御压舱石，逢低布局核心龙头",
        "catalyst_list": ["国家队/险资增持高股息蓝筹", "资本市场维稳座谈会政策预期", "科技股估值杀跌，资金高低切换", "低估值高股息防御属性凸显"],
        "trend": "rising"
    }
    new_b.append(dividend_topic)
    
    baijiu_topic = {
        "id": "topic_b011",
        "name": "白酒消费（蓝筹白马）",
        "level": "B",
        "total_score": 72,
        "dimension_scores": {
            "policy": 70, "industry": 75, "capital": 88, "sentiment": 82,
            "valuation": 80, "catalyst": 60, "market": 85
        },
        "icon": "🍶",
        "color": "red",
        "core_logic": "B级防御蓝筹方向：7/20贵州茅台大涨近6%，古井贡酒/威龙股份涨停，避险资金涌入蓝筹消费。依靠基本面和低波动属性承接科技股出逃资金。白酒板块业绩确定性强、现金流稳定、估值合理，在市场剧烈波动期具备防御配置价值。北向资金逆势净流入主要加仓白酒金融等核心权重。",
        "core_stocks": ["贵州茅台", "古井贡酒", "五粮液", "泸州老窖", "山西汾酒", "威龙股份", "舍得酒业"],
        "recent_performance": "今日白酒蓝筹强势上涨，茅台大涨近6%，古井贡酒/威龙股份涨停",
        "risk_note": "消费复苏力度存疑，纯防御性上涨，空间有限",
        "operation_strategy": "B级防御配置：5%-10%仓位，蓝筹白马作为防御配置",
        "catalyst_list": ["北向资金逆势加仓白酒蓝筹", "避险资金涌入消费白马", "消费扩大十五五规划预期", "业绩确定性强估值合理"],
        "trend": "rising"
    }
    new_b.append(baijiu_topic)
    
    storage_added = False
    for t in b_topics:
        name = t.get('name', '')
        if name == '影视院线/传媒（暑期档）':
            t['total_score'] = 68
            t['dimension_scores']['capital'] = 75
            t['core_logic'] = '暑期档催化+AI降本双逻辑延续，但受市场整体情绪拖累。7/20板块随大盘冲高回落，但相对科技股仍有防御属性。暑期档票房超33亿反超去年，《功夫女足》等头部影片表现亮眼。AI影视制作降本增效逻辑持续。'
            t['recent_performance'] = '今日冲高回落，整体相对抗跌，暑期档催化仍在'
            t['operation_strategy'] = 'B级题材性机会：3%-5%仓位博弈暑期档，快进快出'
            new_b.append(t)
        elif name == '端侧AI/AI应用（软件端）':
            t['total_score'] = 62
            t['dimension_scores']['capital'] = 60
            t['dimension_scores']['sentiment'] = 55
            t['core_logic'] = '科技赛道中相对抗跌方向，但7/20随科技板块整体跳水也难独善其身。端侧AI备案公示+AI应用政策落地逻辑仍在，但市场情绪极差时资金从所有科技方向撤离。智度股份等前期强势股补跌。等待市场企稳后，端侧AI仍是科技反弹先锋。'
            t['recent_performance'] = '今日随科技板块整体跳水，前期强势股补跌，相对跌幅小于硬件端'
            t['operation_strategy'] = 'B级观察：3%-5%仓位，等待市场企稳后再布局'
            t['trend'] = 'falling'
            new_b.append(t)
        elif name == '半导体设备/先进封装':
            t['level'] = 'C'
            t['total_score'] = 55
            t['dimension_scores']['capital'] = 55
            t['dimension_scores']['sentiment'] = 40
            t['core_logic'] = 'C级观望（从B下调）：半导体设备国产替代逻辑坚定，但短期板块情绪彻底崩塌。7/20长电科技/深科技跌停，圣晖集成继续大跌，整个半导体板块-5.61%。澜起科技事件余震+长鑫上市虹吸+机构集中兑现，三重利空叠加。需等待板块大幅缩量+情绪企稳，中长期国产替代逻辑不变。'
            t['recent_performance'] = '今日再遭重创，长电科技/深科技跌停，板块情绪崩塌'
            t['operation_strategy'] = 'C级观望：清仓或底仓2%以下，等待板块企稳信号（缩量+止跌）'
            t['trend'] = 'falling'
            c_topics.append(t)
        elif name == '贵金属/黄金':
            t['total_score'] = 65
            t['core_logic'] = '避险配置选项：全球央行购金+地缘风险+降息预期三重支撑。7/20黄金股相对抗跌但未明显走强，资金更偏好高股息红利和医药防御。中期防御逻辑仍在，可作为组合对冲配置，但短期不是资金首选。'
            t['recent_performance'] = '今日相对抗跌但未走强，资金偏好红利和医药防御'
            t['operation_strategy'] = 'B级防御配置：3%-5%仓位对冲风险'
            new_b.append(t)
        elif name == '房地产（政策博弈）':
            t['level'] = 'C'
            t['total_score'] = 58
            t['core_logic'] = '低位政策博弈，持续性弱。多地购房补贴政策落地，但基本面未改善，纯政策博弈性质。7/20非市场主线。'
            t['operation_strategy'] = 'C级观察：不建议参与'
            c_topics.append(t)
        elif name == '存储芯片/HBM':
            if not storage_added:
                new_b.append(t)
                storage_added = True
        elif name == '油气/煤炭（防御）':
            continue
        else:
            new_b.append(t)
    
    data['b_level_topics'] = new_b
    data['c_level_topics'] = c_topics
    data['system_info']['c_level_count'] = len(c_topics)
    data['system_info']['b_level_count'] = len(new_b)
    
    data['allocation_strategy'] = {
        "market_environment": "极度防御期（指数红个股普跌）",
        "overall_position": "2-3成",
        "core_allocation": "高股息红利(10-15%) + 医药防御(15-20%) + 白酒消费(5-10%)",
        "satellite_allocation": "影视/黄金对冲(5-8%) + 端侧AI观察(3-5%)",
        "cash_position": "50%-70%",
        "risk_control": "科技成长股继续减仓，现金为王，等待市场真正企稳信号（缩量+止跌）。今日267只跌停、3700+个股下跌，恐慌情绪未释放完毕。"
    }
    
    save_json(path, data)
    return True

def update_predictions():
    print("🔮 更新预判验证闭环数据...")
    path = os.path.join(DATA_DIR, 'predictions.json')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    pending = data.get('pending_predictions', [])
    
    if not pending:
        data['system_info']['last_check'] = '2026-07-20'
        data['system_info']['last_check_note'] = '7/20(周一)例行检查：当前无待验证预判。累计验证12条，正确5条/部分5条/错误2条，准确率62.5%，A级分析师。今日科技成长股全面崩盘（半导体-5.61%、PCB-8.4%、267只跌停），印证了"科技股高位估值杀跌"的风险判断。'
        
        new_pred = {
            "id": "pred_20260720_001",
            "title": "科技成长股进入中期调整，高股息红利+医药防御成新主线",
            "level": "A",
            "category": "板块轮动+中期趋势",
            "predict_date": "2026-07-20",
            "verify_date": "2026-07-23",
            "content": "7/20市场极度割裂：沪指+0.85%但3700+个股下跌，267只跌停，半导体指数-5.61%、PCB-8.4%，科技成长股从早盘+3.5%冲高到收盘-5%+，冲高跳水幅度巨大。铜冠铜箔业绩增486%却20cm跌停，典型利好出尽+估值杀跌。国家队护盘指数但小票暴跌，市场风格剧烈切换。预判：科技成长股进入中期调整（幅度30%-50%），高股息红利+医药+消费蓝筹成新共识防御主线，持续时间至少2-3周。",
            "status": "pending",
            "result": "",
            "verify_date_actual": "",
            "result_note": ""
        }
        
        data['pending_predictions'].append(new_pred)
        data['system_info']['pending_count'] = 1
        data['system_info']['last_update'] = '2026-07-20'
        
        print(f"   ℹ️  无到期待验证预判，已新增1条新预判")
    else:
        today = datetime.strptime('2026-07-20', '%Y-%m-%d')
        new_pending = []
        for p in pending:
            verify_date = p.get('verify_date', '')
            if verify_date and datetime.strptime(verify_date, '%Y-%m-%d') <= today:
                pass
            else:
                new_pending.append(p)
        data['pending_predictions'] = new_pending
        data['system_info']['pending_count'] = len(new_pending)
    
    save_json(path, data)
    return True

def update_alerts():
    print("⚡ 更新智能预警系统数据...")
    path = os.path.join(DATA_DIR, 'alerts.json')
    
    alerts_data = {
        "update_time": "2026年07月20日 21:40（周一·今日收盘·科技股全面崩盘+267只跌停）",
        "risk_index": 82,
        "risk_level": "极高风险（科技成长股系统性估值杀跌+267只跌停+3700股下跌+铜冠20cm跌停）",
        "risk_color": "red",
        "suggested_position": "2成以下（现金为王！科技成长股遭遇系统性估值杀跌，267只个股跌停创近期纪录，半导体指数单日-5.61%、PCB板块-8.4%，铜冠铜箔业绩暴增486%却20cm跌停（利好出尽）。国家队护盘指数但小票暴跌，市场极度割裂。严控仓位，优先配置高股息红利+医药防御+消费蓝筹，等待市场真正企稳（缩量+止跌）。）",
        "key_risks": [
            "🚨 267只个股跌停！全市场3700+只股票下跌，涨跌家数1739:3706，赚钱效应极差，典型\"赚指数不赚钱\"",
            "🚨 科技成长股系统性估值杀跌：半导体指数-5.61%（7日累跌超30%）、PCB板块-8.4%、半导体设备/先进封装/MLCC跌幅均超6%",
            "🚨 铜冠铜箔20cm跌停！中报增486%-544%却跌停，核心原因：二季度环比下滑约7%，戳破高增长预期，典型\"利好出尽\"剧本。高点至今已跌48.93%逼近腰斩。",
            "🚨 持仓股全面崩盘：英维克-9.92%跌停（55.46元）、铜冠铜箔-20%跌停（103.24元）、雅克科技-10%跌停（130.50元）、*ST建艺-10%跌停（8.55元），4只全部跌停！",
            "🚨 市场极度割裂：沪指+0.85%、创业板+0.42%，但科创综指大跌2.28%，权重护盘掩盖了小票暴跌真相",
            "⚠️ 长鑫科技上市虹吸效应：科创板新股上市吸引大量资金，科技成长股资金被分流",
            "⚠️ 国家队护盘指数但个股风险巨大：诚通/国新增持蓝筹权重，指数维稳但科技小票无人管",
            "⚠️ 中报业绩验证期：业绩不达预期或增速放缓即跌停，市场容错率极低",
            "✅ 高股息红利成最强防御：油气/煤炭/电力全线大涨，中国海油/中煤能源/华银电力涨停",
            "✅ 白酒蓝筹逆势走强：贵州茅台大涨近6%，古井贡酒/威龙股份涨停，避险资金涌入",
            "✅ 医药继续防御属性：创新药权重托底创业板指，中药/医药商业延续强势",
            "✅ 险资表态：中国太保明确将持续布局科技成长+消费+医药，长线资金支撑",
            "⚠️ 两市成交2.70万亿放量470亿，放量下跌后反弹并非地量筑底，抛压未完全出清"
        ],
        "monitor_cards": [
            {
                "title": "大盘风险监控",
                "icon": "📊",
                "score": 82,
                "level": "极高风险（指数红个股普跌，267只跌停，3700股下跌）",
                "level_color": "red",
                "items": [
                    {"label": "监控内容", "value": "指数涨跌幅、波动率、量能、涨跌家数、跌停数量"},
                    {"label": "风险事件", "value": "7/20周一A股上演极致割裂行情：沪指+0.85%收3796.28点（权重护盘）、深成指-0.71%、创业板+0.42%（创新药权重托底）、科创50+0.19%（但科创综指大跌2.28%）。两市成交2.70万亿放量470亿，涨跌家数1739:3706，267只跌停！核心原因：①国家队增持蓝筹权重维稳指数；②科技成长股系统性估值杀跌（半导体-5.61%、PCB-8.4%）；③长鑫科技上市虹吸效应+机构集中兑现；④中报业绩验证期，增速放缓即跌停；⑤铜冠铜箔业绩暴增却跌停，利好出尽逻辑确认。来源：财联社、东方财富Choice、第一财经"},
                    {"label": "触发条件", "value": "跌停数量超过100只、全市场3000+个股下跌、半导体单日跌幅超5%、单日200+跌停"},
                    {"label": "当前状态", "value": "市场进入极高风险区间，科技成长股系统性估值杀跌趋势明确。指数层面因国家队护盘表现平稳，但个股风险巨大，267只跌停创近期纪录。权重（红利+消费+医药）与小票（科技成长）极致分化。短期仍有下探风险，地量尚未出现（今日放量2.7万亿），说明抛压未出清。操作上仓位降至2成以下，优先配置高股息红利+医药+消费蓝筹防御，科技股继续减仓，现金为王等待企稳。来源：东方财富、财联社、证券时报"}
                ]
            },
            {
                "title": "资金流向监控",
                "icon": "💰",
                "score": 78,
                "level": "高风险（科技股资金大规模出逃，高低切换极致）",
                "level_color": "red",
                "items": [
                    {"label": "监控内容", "value": "主力资金、北向资金、行业资金流向、龙虎榜"},
                    {"label": "风险事件", "value": "资金极端高低切换达到极致。科技成长股资金大规模出逃：电子板块单日净流出预计超400亿，半导体/PCB/光模块成重灾区。北向资金逆势净流入主要加仓白酒、金融、能源等核心权重。内资主力从高位科技硬件赛道全面撤离，调仓至低估值红利+消费蓝筹板块。国家队（诚通/国新）增持央企蓝筹，险资（中国太保）表态持续布局。央行大额逆回购净投放，整体资金面宽松但场内资金主动避险。来源：东方财富Choice、财联社"},
                    {"label": "触发条件", "value": "电子板块连续3日净流出超300亿、北向资金连续3日净流入但个股普跌、主力资金净流出超800亿"},
                    {"label": "当前状态", "value": "资金极致分化格局加剧，科技成长股全面失血，红利+消费+医药成资金避风港。国家队护盘指数但不护科技小票，市场风格剧烈切换。短期科技股资金外流趋势难以逆转，待中报业绩风险释放完毕+板块缩量企稳后，资金有望逐步回流高景气科技赛道。关注明日北向资金流向是否延续、科技板块是否出现缩量止跌信号。来源：证券时报、新浪财经"}
                ]
            },
            {
                "title": "持仓风险监控",
                "icon": "📦",
                "score": 95,
                "level": "极高风险（4只持仓全部跌停，组合单日回撤超预期）",
                "level_color": "red",
                "items": [
                    {"label": "监控内容", "value": "持仓标的价格、涨跌幅、止损状态、资金动向"},
                    {"label": "风险事件", "value": "今日4只持仓全部跌停，为建仓以来最惨烈一日：英维克-9.92%跌停收55.46元（深度破止损-46.8%，再创年内新低）；铜冠铜箔-20% 20cm跌停收103.24元（中报增486%却跌停，利好出尽，高点跌48.93%逼近腰斩）；雅克科技-10%跌停收130.50元（四连跌从209回撤37.6%，浮盈从+90%缩至+20%）；*ST建艺-10%跌停收8.55元（退市风险发酵，浮亏-36.4%）。组合单日回撤幅度巨大，健康分骤降。来源：东方财富、腾讯财经"},
                    {"label": "触发条件", "value": "任意持仓单日跌停、2只以上持仓同时跌停、组合单日回撤超8%、持仓全部破位"},
                    {"label": "当前状态", "value": "持仓风险达到历史最高水平，4只持仓全部跌停！操作策略：①英维克已深度破止损-46.8%，明日开盘无条件清仓；②铜冠铜箔20cm跌停杀跌动能极强，明日若开板立即减仓至底仓以下，跌破90元止盈离场；③雅克科技四连跌停，反弹135-140坚决减仓至底仓，破120止盈离场；④*ST建艺坚决清仓，退市风险敞口必须立即关闭。整体仓位降至0-1成，现金为王，等待市场真正企稳。来源：自研持仓诊断系统"}
                ]
            },
            {
                "title": "外围风险监控",
                "icon": "🌍",
                "score": 50,
                "level": "中风险（外围相对稳定，A股内因主导）",
                "level_color": "yellow",
                "items": [
                    {"label": "监控内容", "value": "美股、港股、汇率、大宗、地缘"},
                    {"label": "风险事件", "value": "外围市场相对稳定，美国CPI降温后美联储降息预期升温，对A股中长期有利。但A股内因（科技股估值杀跌+中报验证+长鑫上市虹吸）主导今日走势。美伊地缘冲突持续但影响减弱，原油价格相对平稳。人民币汇率基本稳定（美元/人民币中间价6.7948）。来源：华尔街见闻、彭博社、新华社"},
                    {"label": "触发条件", "value": "费半单日跌超5%、纳指跌超2%、人民币贬值超500点、原油单日涨超5%"},
                    {"label": "当前状态", "value": "外围流动性环境改善（CPI降温→降息预期）对A股中长期有利，但短期A股内因主导走势（科技估值杀跌+中报业绩验证+风格切换）。今日A股科技股崩盘主要是内部因素，外围并非主要推手。待国内科技股业绩风险释放完毕后，外围利好有望重新发挥作用。关注今晚美股表现、美联储政策信号。来源：新浪财经、财联社"}
                ]
            },
            {
                "title": "板块轮动监控",
                "icon": "🎯",
                "score": 85,
                "level": "极高风险（科技→防御极致切换，半导体单日蒸发万亿市值）",
                "level_color": "red",
                "items": [
                    {"label": "监控内容", "value": "行业涨跌、主线持续性、高低切"},
                    {"label": "风险事件", "value": "今日板块极致分化：领涨（高股息红利+油气煤炭+白酒消费+医药）vs 领跌（PCB-8.4%、半导体-5.61%、先进封装-6%+、光模块/CPO、能源金属）。科技成长股全面崩盘，267只跌停主要集中在电子/半导体/PCB/算力硬件板块。铜冠铜箔业绩暴增486%却20cm跌停，标志着科技成长股从炒预期进入杀估值阶段。资金从高位科技全面切换至低位防御板块（红利+消费+医药），市场风格剧烈切换。来源：东方财富、第一财经、证券时报"},
                    {"label": "触发条件", "value": "科技板块单日跌幅超5%、跌停超100只集中在科技、新主线3日内不熄火确认切换"},
                    {"label": "当前状态", "value": "市场风格已彻底切换：从AI科技成长主导转向高股息红利+医药+消费蓝筹防御主导。科技成长股进入中期调整期，预计幅度30%-50%，持续时间2-3周。存储/半导体/算力硬件等前期主线跌幅巨大，铜冠铜箔高点至今已腰斩。但科技长期逻辑（AI算力+国产替代+存储超级周期）并未逆转，只是估值过高+情绪过热后的系统性回调。等待板块缩量企稳后再评估布局机会，短期坚决回避抄底。来源：36氪、中国商报、财联社"}
                ]
            },
            {
                "title": "制度变革监控",
                "icon": "📜",
                "score": 55,
                "level": "中风险（长鑫科技上市虹吸+国家队护盘+监管维稳）",
                "level_color": "yellow",
                "items": [
                    {"label": "监控内容", "value": "新股上市、国家队行动、监管政策、ST板块"},
                    {"label": "风险事件", "value": "长鑫科技今日科创板上市，作为国内唯一量产主流DRAM的厂商，募资295亿创年内最大IPO，对科技成长股产生显著虹吸效应。国家队（中国诚通+国新控股）持续增持央企蓝筹，累计投入超600亿元护盘。证监会召开上市公司/券商/基金座谈会维稳市场。中国太保等险资表态将持续布局。ST板块持续弱势，*ST建艺等退市风险股连续跌停。来源：证监会、上交所、新华社"},
                    {"label": "触发条件", "value": "大额IPO抽血、监管政策转向、ST板块集体跌停、退市风险扩散"},
                    {"label": "当前状态", "value": "政策面整体维稳导向明确，国家队+险资持续进场护盘指数。但护盘对象集中在蓝筹权重，科技小票不在护盘范围内，导致指数稳个股惨。长鑫科技上市短期虹吸科技股资金，但长期利好存储产业链。中报业绩最后披露期，业绩雷仍在释放。关注后续维稳政策加码、产业支持政策出台。来源：证监会、财联社、证券时报"}
                ]
            },
            {
                "title": "产业&政策监控",
                "icon": "🏭",
                "score": 60,
                "level": "中高风险（产业政策持续但短期不敌估值杀跌）",
                "level_color": "orange",
                "items": [
                    {"label": "监控内容", "value": "产业政策、重大合同、行业催化、重要会议"},
                    {"label": "风险事件", "value": "产业政策面整体偏暖：算力网建设+8000亿特别国债长期不变、存储超级周期产业逻辑未改、半导体国产替代加速推进。但短期市场情绪主导一切，产业逻辑敌不过估值杀跌。铜冠铜箔中报增486%却跌停，说明市场对科技股的定价逻辑已从炒预期转向杀估值。中长期产业趋势向上，但短期需等待情绪企稳+估值合理。消费扩大十五五规划利好消费板块。来源：国家统计局、工信部、证券时报"},
                    {"label": "触发条件", "value": "重大产业政策出台、黑天鹅事件、行业突发利好"},
                    {"label": "当前状态", "value": "产业政策面整体偏暖，但短期市场情绪主导科技股走势。AI算力、存储、半导体国产替代等长期逻辑未改，只是估值过高需要时间消化。中报业绩验证是当前核心矛盾，业绩增速放缓或不及预期的标的直接跌停（如铜冠铜箔）。等待中报业绩全部披露完毕+科技股缩量企稳，是下一轮布局的信号。来源：新华社、工信部、财联社"}
                ]
            }
        ]
    }
    
    save_json(path, alerts_data)
    return True

def main():
    print("=" * 60)
    print("🔧 每日系统维护 - 数据更新")
    print(f"⏰ 执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)
    print()
    
    results = {}
    results['portfolio'] = update_portfolio()
    print()
    results['topics'] = update_topics()
    print()
    results['predictions'] = update_predictions()
    print()
    results['alerts'] = update_alerts()
    print()
    
    print("=" * 60)
    success = sum(1 for v in results.values() if v)
    print(f"✅ 数据更新完成，成功 {success}/{len(results)} 项")
    print("=" * 60)

if __name__ == '__main__':
    main()
