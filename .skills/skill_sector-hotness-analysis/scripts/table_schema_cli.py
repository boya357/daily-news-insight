import argparse
import sys
import pandas as pd

from finance_query import FinanceMCP


def _parse_tables(s: str):
    parts = [p for p in [x.strip() for x in s.replace(",", " ").split()] if p]
    if not parts:
        raise ValueError("至少需要一个表名")
    return parts


def _query_table_exists(mcp: FinanceMCP, table: str) -> bool:
    sql = f"""
    SELECT TABLE_NAME
    FROM information_schema.tables
    WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = '{table}'
    LIMIT 1
    """
    df = mcp.query(sql)
    return df is not None and not df.empty


def _query_table_schema(mcp: FinanceMCP, table: str) -> pd.DataFrame:
    sql = f"""
    SELECT
        COLUMN_NAME,
        DATA_TYPE,
        IS_NULLABLE,
        COLUMN_KEY,
        COLUMN_DEFAULT,
        EXTRA,
        COLUMN_COMMENT
    FROM information_schema.columns
    WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = '{table}'
    ORDER BY ORDINAL_POSITION
    """
    df = mcp.query(sql)
    if df is None:
        return pd.DataFrame()
    df.insert(0, "TableName", table)
    return df


def main():
    parser = argparse.ArgumentParser(
        prog="table-schema",
        description="查看指定DB表的Schema信息"
    )
    parser.add_argument("--tables", required=True, help="表名列表，逗号或空格分隔，如 dz_dailyquote,secumain")
    parser.add_argument("--format", choices=["csv", "table"], default="csv")
    args = parser.parse_args()

    try:
        tables = _parse_tables(args.tables)
    except Exception as e:
        print(f"❌ 参数错误: {e}")
        sys.exit(1)

    mcp = FinanceMCP()
    try:
        mcp.connect()
    except Exception as e:
        print(f"❌ 连接失败: {e}")
        sys.exit(1)

    all_rows = []
    for t in tables:
        try:
            if not _query_table_exists(mcp, t):
                msg = f"❌ 表不存在: {t}"
                if args.format == "csv":
                    print(msg, file=sys.stderr)
                else:
                    print(msg)
                continue
            df_schema = _query_table_schema(mcp, t)
        except Exception as e:
            msg = f"❌ 查询失败: {e}"
            if args.format == "csv":
                print(msg, file=sys.stderr)
            else:
                print(msg)
            continue
        if df_schema.empty:
            if args.format == "table":
                print(f"=== 表: {t} ===")
                print("无字段信息")
            else:
                print(f"❌ 表无字段信息: {t}", file=sys.stderr)
            continue
        if args.format == "table":
            print(f"=== 表: {t} ===")
            print(df_schema.to_csv(sep="\t", index=False))
        else:
            all_rows.append(df_schema)
    if args.format == "csv":
        if all_rows:
            out = pd.concat(all_rows, ignore_index=True)
            print(out.to_csv(index=False))
        else:
            print("无结果")


if __name__ == "__main__":
    main()
