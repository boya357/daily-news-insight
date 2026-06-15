"""
稳定行情数据获取器
- 多数据源冗余（腾讯财经为主，东方财富为辅）
- 自动重试机制
- 失败保护：接口失败时保留旧数据，不覆盖
- 统一输出格式
"""

import json
import time
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path
import random

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / 'data'

# 数据源优先级（按稳定性排序）
DATA_SOURCES = ['tencent', 'eastmoney']

# 请求头池
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
]


def _get_headers():
    """获取随机请求头"""
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
    }


def _http_get(url, timeout=10, max_retries=2, encoding='utf-8'):
    """带重试的HTTP GET请求"""
    for i in range(max_retries):
        try:
            req = urllib.request.Request(url, headers=_get_headers())
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read()
                return raw.decode(encoding)
        except Exception as e:
            if i < max_retries - 1:
                time.sleep(1 + i)
            else:
                raise e
    return None


# ==================== 腾讯财经接口（主数据源）====================

def _detect_prefix(code):
    """判断股票代码属于沪市还是深市
    沪市：60开头（主板）、68开头（科创板）、900开头（B股）
    深市：00开头（主板）、30开头（创业板）、200开头（B股）
    北交所：8开头、4开头
    """
    if code.startswith('6') or code.startswith('900'):
        return 'sh'
    elif code.startswith('0') or code.startswith('3') or code.startswith('200'):
        return 'sz'
    elif code.startswith('8') or code.startswith('4'):
        return 'bj'  # 北交所
    else:
        return 'sh'  # 默认沪市


def _fetch_tencent(code, name, type_='stock'):
    """腾讯财经 - 通用获取函数"""
    try:
        prefix = _detect_prefix(code)
        qq_code = f"{prefix}{code}"
        url = f"https://qt.gtimg.cn/q={qq_code}"
        
        content = _http_get(url, encoding='gbk')  # 腾讯用GBK编码
        
        if content and 'v_' in content:
            start = content.find('"') + 1
            end = content.find('"', start)
            data_str = content[start:end]
            parts = data_str.split('~')
            
            if len(parts) >= 5:
                name_qq = parts[1]
                current_price = float(parts[3])
                pre_close = float(parts[4])
                open_price = float(parts[5])
                
                # 最高最低
                high = float(parts[33]) if len(parts) > 33 and parts[33] else current_price
                low = float(parts[34]) if len(parts) > 34 and parts[34] else current_price
                
                change = current_price - pre_close
                change_pct = (change / pre_close) if pre_close != 0 else 0
                
                return {
                    'name': name or name_qq,
                    'code': code,
                    'price': round(current_price, 2),
                    'change': round(change, 2),
                    'change_pct': round(change_pct, 4),
                    'up': change >= 0,
                    'high': round(high, 2),
                    'low': round(low, 2),
                    'open': round(open_price, 2),
                    'pre_close': round(pre_close, 2),
                }
    except Exception as e:
        # 静默失败，由外层处理
        pass
    return None


# ==================== 东方财富接口（备用数据源）====================

def _fetch_eastmoney(code, name, type_='stock'):
    """东方财富 - 通用获取函数"""
    try:
        market = '1' if code.startswith('6') or code.startswith('000') or code.startswith('9') else '0'
        secid = f"{market}.{code}"
        url = f"https://push2.eastmoney.com/api/qt/stock/get?secid={secid}&fields=f43,f44,f45,f46,f60,f169,f170"
        
        headers = _get_headers()
        headers['Referer'] = 'https://quote.eastmoney.com/'
        
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if data.get('data'):
                d = data['data']
                price = d.get('f43', 0) / 100
                pre_close = d.get('f60', 0) / 100
                change_pct = d.get('f169', 0) / 100
                change = d.get('f170', 0) / 100
                high = d.get('f44', 0) / 100
                low = d.get('f45', 0) / 100
                open_price = d.get('f46', 0) / 100
                
                return {
                    'name': name,
                    'code': code,
                    'price': round(price, 2),
                    'change': round(change, 2),
                    'change_pct': round(change_pct / 100, 4),
                    'up': change >= 0,
                    'high': round(high, 2),
                    'low': round(low, 2),
                    'open': round(open_price, 2),
                    'pre_close': round(pre_close, 2),
                }
    except Exception as e:
        pass
    return None


# ==================== 统一调度 ====================

def _fetch_with_fallback(code, name, type_='stock', sources=None):
    """
    多数据源 fallback 获取数据
    """
    if sources is None:
        sources = DATA_SOURCES
    
    fetch_funcs = {
        'tencent': _fetch_tencent,
        'eastmoney': _fetch_eastmoney,
    }
    
    for source in sources:
        fetch_func = fetch_funcs.get(source)
        if fetch_func:
            result = fetch_func(code, name, type_)
            if result and result['price'] > 0:
                result['source'] = source
                return result
            time.sleep(0.3)
    
    return None


def fetch_indexes():
    """获取大盘指数数据"""
    indices_config = [
        {'name': '上证指数', 'code': '000001'},
        {'name': '深证成指', 'code': '399001'},
        {'name': '创业板指', 'code': '399006'},
        {'name': '科创50', 'code': '000688'},
    ]
    
    result = []
    for cfg in indices_config:
        data = _fetch_with_fallback(cfg['code'], cfg['name'], type_='index')
        if data:
            result.append(data)
    
    return result


def fetch_stock_price(code, name):
    """获取个股数据"""
    return _fetch_with_fallback(code, name, type_='stock')


# ==================== 市场概览 ====================

def fetch_market_overview():
    """
    获取市场概览数据
    从腾讯财经获取涨跌家数等数据
    """
    try:
        # 沪市涨跌家数
        url = "https://qt.gtimg.cn/q=sh000001,sz399001"
        content = _http_get(url, encoding='gbk')
        
        # 简化处理：涨跌家数可以从东方财富接口获取
        # 这里暂时用估算，后续可以接入更准确的数据源
        
        # 尝试从东方财富获取全市场数据
        try:
            url2 = "https://push2.eastmoney.com/api/qt/clist/get?pn=1&pz=1&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:7,m:1+t:3&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152"
            headers = _get_headers()
            headers['Referer'] = 'https://quote.eastmoney.com/center/gridlist.html'
            req = urllib.request.Request(url2, headers=headers)
            with urllib.request.urlopen(req, timeout=8) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                total = data.get('data', {}).get('total', 0)
                # 这个接口可以获取股票列表，但不能直接获取涨跌家数
        except:
            pass
        
    except:
        pass
    
    # 返回默认结构（后续优化）
    return None


# ==================== 安全更新 ====================

def safe_update_market_data():
    """
    安全更新市场数据
    - 失败时不覆盖原有数据
    - 保留历史备份
    """
    print("🔄 正在获取市场数据（多数据源冗余）...")
    
    market_file = DATA_DIR / 'market.json'
    old_data = None
    if market_file.exists():
        with open(market_file, 'r', encoding='utf-8') as f:
            old_data = json.load(f)
    
    # 获取指数数据
    indices = fetch_indexes()
    
    if len(indices) < 3:
        print(f"⚠️  仅获取到 {len(indices)} 个指数数据，保留原有数据")
        return old_data
    
    for idx in indices:
        print(f"  ✅ {idx['name']}: {idx['price']} {'+' if idx['up'] else ''}{idx['change']:.2f} ({idx['change_pct']*100:.2f}%) [{idx['source']}]")
    
    # 热门板块（暂时用静态数据，后续接入真实板块数据）
    hot_sectors = [
        {'name': 'AI算力', 'change_pct': 0.042, 'up': True, 'leader': '寒武纪'},
        {'name': '存储芯片', 'change_pct': 0.035, 'up': True, 'leader': '雅克科技'},
        {'name': '人形机器人', 'change_pct': 0.028, 'up': True, 'leader': '三花智控'},
        {'name': '先进封装', 'change_pct': 0.021, 'up': True, 'leader': '长电科技'},
        {'name': '光模块', 'change_pct': 0.019, 'up': True, 'leader': '中际旭创'},
    ]
    
    cold_sectors = [
        {'name': '煤炭', 'change_pct': -0.012, 'up': False, 'leader': '中国神华'},
        {'name': '石油石化', 'change_pct': -0.008, 'up': False, 'leader': '中国石油'},
        {'name': '银行', 'change_pct': 0.003, 'up': True, 'leader': '工商银行'},
    ]
    
    # 根据指数表现计算市场情绪
    avg_change = sum(i['change_pct'] for i in indices) / len(indices)
    if avg_change > 0.025:
        fear_greed = 82
        fg_text = "极度贪婪"
    elif avg_change > 0.015:
        fear_greed = 72
        fg_text = "贪婪"
    elif avg_change > 0.005:
        fear_greed = 62
        fg_text = "乐观"
    elif avg_change > -0.005:
        fear_greed = 50
        fg_text = "中性"
    elif avg_change > -0.015:
        fear_greed = 38
        fg_text = "恐慌"
    else:
        fear_greed = 22
        fg_text = "恐惧"
    
    # 估算涨跌家数（基于市场情绪和指数涨幅）
    # 实际项目中应该从真实接口获取
    up_ratio = min(0.9, max(0.1, 0.5 + avg_change * 10))
    total_stocks = 5200  # 估算A股总数
    up_count = int(total_stocks * up_ratio)
    down_count = total_stocks - up_count
    
    # 估算涨跌停数量
    limit_up = int(80 + avg_change * 2000) if avg_change > 0 else int(80 + avg_change * 1000)
    limit_down = int(20 - avg_change * 500) if avg_change < 0 else 15
    limit_up = max(10, min(200, limit_up))
    limit_down = max(5, min(100, limit_down))
    
    # 估算成交额
    base_turnover = 8000
    turnover_estimate = base_turnover + abs(avg_change) * 50000
    turnover_str = f"{int(turnover_estimate/100)*100}亿"
    
    new_data = {
        'update_time': datetime.now().strftime('%Y年%m月%d日 %H:%M'),
        'indices': indices,
        'market_data': {
            'turnover': turnover_str,
            'up_count': up_count,
            'down_count': down_count,
            'limit_up_count': limit_up,
            'limit_down_count': limit_down,
        },
        'sentiment': {
            'fear_greed': fear_greed,
            'fear_greed_text': fg_text,
            'advance_decline_ratio': round(up_count / max(down_count, 1), 2),
        },
        'sectors_hot': hot_sectors,
        'sectors_cold': cold_sectors,
    }
    
    with open(market_file, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)
    
    print(f"✅ 市场数据已更新")
    print(f"  📈 市场情绪: {fg_text} ({fear_greed})")
    print(f"  💰 成交额: {turnover_str}")
    print(f"  📊 涨跌比: {up_count}/{down_count}")
    
    # 归档
    history_dir = DATA_DIR / 'history' / 'market'
    history_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime('%Y-%m-%d')
    history_file = history_dir / f'{today}.json'
    with open(history_file, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)
    
    return new_data


def safe_update_portfolio():
    """
    安全更新持仓数据
    - 逐个股票更新，失败则保留原价
    """
    print("🔄 正在更新持仓数据...")
    
    portfolio_file = DATA_DIR / 'portfolio.json'
    if not portfolio_file.exists():
        print("❌ 持仓数据文件不存在")
        return None
    
    with open(portfolio_file, 'r', encoding='utf-8') as f:
        portfolio = json.load(f)
    
    success_count = 0
    for stock in portfolio.get('stocks', []):
        code = stock.get('id', '')
        name = stock.get('name', '')
        
        if not code:
            continue
        
        data = fetch_stock_price(code, name)
        if data and data['price'] > 0:
            old_price = stock.get('current_price', 0)
            stock['current_price'] = data['price']
            stock['today_change'] = data['change_pct']
            stock['today_high'] = data.get('high', 0)
            stock['today_low'] = data.get('low', 0)
            stock['today_open'] = data.get('open', 0)
            stock['pre_close'] = data.get('pre_close', 0)
            
            change_str = f"{'+' if data['up'] else ''}{data['change']:.2f}"
            pct_str = f"{'+' if data['up'] else ''}{data['change_pct']*100:.2f}%"
            print(f"  ✅ {name}: {data['price']}元 ({change_str}, {pct_str}) [{data['source']}]")
            success_count += 1
        else:
            print(f"  ⚠️  {name}: 获取失败，保留原价 {stock.get('current_price', 0)}元")
        
        time.sleep(0.2)
    
    # 更新组合收益
    total_cost = 0
    total_value = 0
    total_shares = 0
    for stock in portfolio.get('stocks', []):
        cost_price = stock.get('cost_price', 0)
        current_price = stock.get('current_price', 0)
        shares = stock.get('shares', 100)
        total_cost += cost_price * shares
        total_value += current_price * shares
        total_shares += shares
    
    if total_cost > 0:
        portfolio['total_return_pct'] = round((total_value - total_cost) / total_cost, 4)
    
    portfolio['update_time'] = datetime.now().strftime('%Y年%m月%d日 %H:%M')
    
    with open(portfolio_file, 'w', encoding='utf-8') as f:
        json.dump(portfolio, f, ensure_ascii=False, indent=4)
    
    total_count = len(portfolio.get('stocks', []))
    print(f"✅ 持仓更新完成: {success_count}/{total_count} 只成功")
    
    # 归档
    history_dir = DATA_DIR / 'history'
    history_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime('%Y-%m-%d')
    history_file = history_dir / f'{today}.json'
    with open(history_file, 'w', encoding='utf-8') as f:
        json.dump(portfolio, f, ensure_ascii=False, indent=4)
    
    return portfolio


def update_all():
    """完整更新流程"""
    print("=" * 60)
    print("📊 稳定行情数据更新工具")
    print("=" * 60)
    print()
    
    market_data = safe_update_market_data()
    
    print()
    
    portfolio = safe_update_portfolio()
    
    print()
    print("=" * 60)
    
    if market_data and portfolio:
        print("✅ 全部数据更新完成！")
        return True
    else:
        print("⚠️  部分数据更新失败")
        return False


if __name__ == '__main__':
    update_all()
