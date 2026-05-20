import argparse
import re
import sys
import pandas as pd

from finance_query import FinanceMCP

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

SECU_CATEGORY_MAP = {
    1: "A股",
    2: "B股",
    4: "大盘",
    5: "国债回购",
    6: "国债现货",
    7: "金融债券",
    8: "开放式基金",
    9: "可转换债券",
    10: "其他",
    11: "企业债券",
    12: "企业债券回购",
    13: "投资基金",
    14: "央行票据",
    15: "深市代理沪市股票",
    16: "沪市代理深市股票",
    17: "资产支持证券",
    18: "资产证券化产品",
    19: "买断式回购",
    20: "衍生权证",
    21: "股本权证",
    23: "商业银行定期存款",
    26: "收益增长线",
    27: "新质押式回购",
    28: "地方政府债",
    29: "可交换公司债",
    30: "拆借",
    31: "信用风险缓释工具",
    32: "浮息债计息基准利率",
    33: "定期存款凭证",
    35: "大额存款凭证",
    36: "债券借贷",
    37: "存款类机构质押式回购",
    38: "存款类机构信用拆借",
    39: "现货",
    40: "货币对",
    41: "中国存托凭证",
    42: "协议回购",
    43: "三方回购",
    44: "利率互换品种",
    45: "标准利率互换合约",
    46: "报价回购",
    47: "标准化票据",
    55: "优先股",
    79: "深市代理港交所股票",
    80: "沪市代理港交所股票",
    211: "自贸区债",
}

LISTED_SECTOR_MAP = {
    1: "主板",
    2: "中小企业板",
    3: "三板",
    4: "其他",
    5: "大宗交易系统",
    6: "创业板",
    7: "科创板",
    8: "北交所股票",
}

LISTED_STATE_MAP = {
    1: "上市",
    3: "暂停",
    5: "终止",
    9: "其他",
}


def _parse_keywords(s: str):
    parts = [p for p in re.split(r"[,]+", s.strip()) if p]
    return parts


def _add_market_names(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    def map_market(v):
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
    if "SecuMarket" in df.columns:
        df["SecuMarketName"] = df["SecuMarket"].map(map_market)
    return df


def _add_enum_desc(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    def map_int(v):
        try:
            import math
            if v is None:
                return None
            if isinstance(v, float) and math.isnan(v):
                return None
        except Exception:
            pass
        try:
            return int(v)
        except Exception:
            return None
    if "SecuCategory" in df.columns:
        df["SecuCategoryDesc"] = df["SecuCategory"].map(lambda v: SECU_CATEGORY_MAP.get(map_int(v), str(v)))
    if "ListedSector" in df.columns:
        df["ListedSectorDesc"] = df["ListedSector"].map(lambda v: LISTED_SECTOR_MAP.get(map_int(v), str(v)))
    if "ListedState" in df.columns:
        df["ListedStateDesc"] = df["ListedState"].map(lambda v: LISTED_STATE_MAP.get(map_int(v), str(v)))
    return df

def _normalize_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    for col in [
        "innercode",
        "SecuMarket",
        "SecuCategory",
        "ListedSector",
        "ListedState",
    ]:
        if col in df.columns:
            try:
                df[col] = df[col].astype("Int64")
            except Exception:
                pass
    return df


def main():
    parser = argparse.ArgumentParser(
        prog="security-lookup",
        description="通过名称或股票代码在多市场主表定位证券并返回所属市场"
    )
    parser.add_argument("--keywords", required=True, help="名称/代码，逗号分隔，如 AAPL,港交所,600000")
    parser.add_argument("--format", choices=["csv", "table"], default="csv")
    parser.add_argument("--limit", type=int, default=100, help="每个表的最大返回条数")
    args = parser.parse_args()

    try:
        keywords = _parse_keywords(args.keywords)
    except Exception as e:
        print(f"❌ 参数错误: {e}")
        sys.exit(1)

    mcp = FinanceMCP()
    try:
        mcp.connect()
        print(f"🔍 Searching for: {keywords}")
        df = mcp.lookup(keywords, limit=args.limit)
        
        if df is None or df.empty:
            print("无结果")
        else:
            out = df
            # Deduplicate if needed
            if "SecuCode" in out.columns and "SecuMarket" in out.columns:
                out = out.drop_duplicates(subset=["SecuCode", "SecuMarket"], keep="first")
            
            out = _add_market_names(out)
            out = _add_enum_desc(out)
            out = _normalize_dtypes(out)

            # Filter columns
            target_columns = [
                "ChiName", "ChiNameAbbr", "CompanyCode", "EngName", 
                "EngNameAbbr", "innercode", "SecuCode", "SecuMarketName", 
                "SecuCategoryDesc", "ListedSectorDesc", "ListedStateDesc"
            ]
            existing_cols = [c for c in target_columns if c in out.columns]
            if existing_cols:
                out = out[existing_cols]

            if args.format == "table":
                print(out.to_csv(sep="\t", index=False))
            else:
                print(out.to_csv(index=False))
                
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
