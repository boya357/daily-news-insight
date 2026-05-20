import argparse
import re
import sys

from datetime import datetime


# 使用搜索确认后的精确代码查询
from finance_query import FinanceMCP, query_trading_days


 


MARKET_MAP = {
    10: "上海期货交易所",
    12: "中国银行间外汇市场",
    13: "大连商品交易所",
    14: "上海黄金交易所",
    15: "郑州商品交易所",
    16: "上海票据交易所",
    18: "北京证券交易所",
    40: "芝加哥商业交易所",
    49: "澳大利亚证券交易所",
    50: "新西兰证券交易所",
    52: "埃及开罗及亚历山大证券交易所",
    54: "阿根廷布宜诺斯艾利斯证券交易所",
    55: "巴西圣保罗证券交易所",
    56: "墨西哥证券交易所",
    65: "印度尼西亚证券交易所",
    66: "泰国证券交易所",
    67: "韩国首尔证券交易所",
    68: "东京证券交易所",
    69: "新加坡证券交易所",
    70: "台湾证券交易所",
    71: "柜台交易市场",
    72: "香港联交所",
    73: "一级市场",
    75: "亚洲其他交易所",
    76: "美国证券交易所",
    77: "美国纳斯达克证券交易所",
    78: "纽约证券交易所",
    79: "美国其他交易市场",
    80: "加拿大多伦多证券交易所",
    81: "三板市场",
    83: "上海证券交易所",
    84: "其他市场",
    85: "伦敦证券交易所",
    86: "法国巴黎证券交易所",
    87: "德国法兰克福证券交易所",
    88: "欧洲其他交易所",
    89: "银行间债券市场",
    90: "深圳证券交易所",
    93: "上海银行间同业拆借市场",
    94: "瑞士证券交易所",
    95: "荷兰阿姆斯特丹证券交易所",
    96: "约翰内斯堡证券交易所",
    99: "东京同业拆借市场",
    100: "美国国债回购市场",
    101: "伦敦银行同业拆借市场",
    102: "香港银行同业拆借市场",
    103: "新加坡银行同业拆借市场",
    104: "中国银行同业拆借市场",
    105: "欧元银行同业拆借市场",
    106: "布鲁塞尔证券交易所",
    107: "雅加达证券交易所",
    110: "以色列特拉维夫证券交易所",
    161: "意大利证券交易所",
    162: "哥本哈根证券交易所",
    180: "挪威奥斯陆证券交易所",
    200: "斯德哥尔摩证券交易所",
    202: "伊斯坦布尔证券交易所",
    210: "印度国家证券交易所",
    230: "奥地利维也纳证券交易所",
    240: "西班牙马德里证券交易所",
    260: "爱尔兰证券交易所",
    280: "菲律宾证券交易所",
    310: "机构间私募产品报价与服务系统",
    320: "俄罗斯莫斯科证券交易所",
    390: "里斯本证券交易所",
    400: "芝加哥期权交易所",
    620: "胡志明市证券交易所",
    630: "沪市代理深市市场",
    631: "沪市代理港交所市场",
    640: "深市代理沪市市场",
    641: "深市代理港交所市场",
    650: "国际外汇市场(晨星)",
    653: "上海环境能源交易所",
    654: "北京绿色交易所",
    655: "天津碳排放权交易中心",
    657: "湖北碳排放权交易中心",
    658: "重庆碳排放权交易中心",
    659: "四川联合环境交易所",
    660: "广州碳排放权交易所",
    661: "海峡股权交易中心",
    662: "深圳排放权交易所",
    663: "欧洲能源交易所",
    664: "全国碳排放权交易",
    666: "布达佩斯证券交易所",
    667: "全国温室气体自愿减排交易市场",
    66302: "韩国ETS",
    66303: "加拿大魁北克Cap-and-Trade(CaT)",
    66305: "美国区域温室气体倡议（RGGI）",
}

def _safe_market_name(v):
    try:
        import math
        if v is None:
            return "未知市场"
        if isinstance(v, float) and math.isnan(v):
            return "未知市场"
    except Exception:
        pass
    try:
        i = int(v)
    except Exception:
        return str(v)
    return MARKET_MAP.get(i, str(v))

def _parse_dates(dates_str):
    parts = [p for p in re.split(r"[,\s]+", dates_str.strip()) if p]
    parsed = []
    for p in parts:
        dt = datetime.strptime(p, "%Y-%m-%d")
        parsed.append(dt.strftime("%Y-%m-%d"))
    return parsed


def _add_market_names(df):
    if df.empty:
        return df
    df["SecuMarketName"] = df["SecuMarket"].map(_safe_market_name)
    return df

def _normalize_dtypes(df):
    if df.empty:
        return df
    try:
        df["SecuMarket"] = df["SecuMarket"].astype("Int64")
    except Exception:
        pass
    for col in [
        "IfTradingDay",
        "IfWeekEnd",
        "IfMonthEnd",
        "IfQuarterEnd",
        "IfYearEnd",
    ]:
        if col in df.columns:
            try:
                df[col] = df[col].astype("Int64")
            except Exception:
                pass
    return df

def _translate_enums(df):
    if df.empty:
        return df
    def trans(v):
        try:
            i = int(v)
        except Exception:
            return str(v)
        if i == 1:
            return "是"
        if i == 2:
            return "否"
        return str(v)
    for col in [
        "IfTradingDay",
        "IfWeekEnd",
        "IfMonthEnd",
        "IfQuarterEnd",
        "IfYearEnd",
    ]:
        if col in df.columns:
            df[col + "Desc"] = df[col].map(trans)
    return df


def main():
    parser = argparse.ArgumentParser(
        prog="trading-days",
        description="查询指定日期在各市场是否为交易日"
    )
    parser.add_argument("--dates", required=True, help="日期列表，逗号或空格分隔，如 2025-01-02,2025-01-03")
    parser.add_argument("--format", choices=["csv", "table"], default="csv")
    parser.add_argument("--include-flags", action="store_true")
    args = parser.parse_args()

    try:
        dates = _parse_dates(args.dates)
    except Exception as e:
        print(f"❌ 参数错误: {e}")
        sys.exit(1)

    mcp = FinanceMCP()
    try:
        mcp.connect()
    except Exception as e:
        print(f"❌ 连接失败: {e}")
        sys.exit(1)

    try:
        df = query_trading_days(mcp, dates, markets=None, include_flags=args.include_flags)
    except Exception as e:
        print(f"❌ 查询失败: {e}")
        sys.exit(1)

    if df.empty:
        print("无结果")
        return

    df = _add_market_names(df)
    df = _normalize_dtypes(df)
    df = _translate_enums(df)
    if args.format == "table":
        print(df.to_csv(sep="\t", index=False))
    else:
        print(df.to_csv(index=False))


if __name__ == "__main__":
    main()
