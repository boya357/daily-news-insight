
"""
MySQL Finance Query - 金融数据查询分析引擎
基于Finance Data MCP的HTTP API实现
"""

import json
import threading
import time
import random
import pandas as pd
from io import BytesIO, StringIO
import base64
import os
from coze_workload_identity import requests


class FinanceMCP:
    """Finance MCP HTTP客户端"""
    
    def __init__(self):
        # 从环境变量读取配置
        self.base_url = os.environ.get("FINANCE_MCP_BASE_URL", "http://ep-13fr1vonp7ksg3n6nu5313wvy.epsvc-mj52e66ru29s5smt1afxwuev.cn-beijing.privatelink.volces.com")
        # 从环境变量读取token
        self.token = os.getenv("COZE_FINANCE_MCP_7595560047095250979")
        if not self.token:
            raise ValueError("缺少必要的凭证配置：COZE_FINANCE_MCP_7595560047095250979")
        if not self.token:
            raise ValueError("❌ 缺少必要的环境变量 FINANCE_MCP_TOKEN")
        self.endpoint_path = None
        self.responses = []
        self.initialized = False
        self._endpoint_ready = threading.Event()
        self._responses_cond = threading.Condition()
        self._listener_thread = None
        
    def connect(self):
        """建立SSE连接"""
        def sse_listener():
            sse_url = f"{self.base_url}/sse"
            params = {"token": self.token}
            while True:
                try:
                    response = requests.get(sse_url, params=params, stream=True, timeout=(10, 300))
                    for line in response.iter_lines():
                        if not line:
                            continue
                        decoded = line.decode('utf-8', errors='ignore')
                        if decoded.startswith('data: /messages'):
                            self.endpoint_path = decoded.replace('data: ', '').strip()
                            self._endpoint_ready.set()
                            continue
                        if decoded.startswith('data: {'):
                            try:
                                data = json.loads(decoded.replace('data: ', ''))
                            except Exception:
                                continue
                            with self._responses_cond:
                                self.responses.append(data)
                                if len(self.responses) > 2000:
                                    self.responses = self.responses[-1000:]
                                self._responses_cond.notify_all()
                except Exception:
                    time.sleep(0.5 + random.random())
        
        self._listener_thread = threading.Thread(target=sse_listener, daemon=True)
        self._listener_thread.start()
        
        if not self._endpoint_ready.wait(timeout=10):
            raise Exception("❌ MCP连接超时")
        
        self._initialize()
        return True
    
    def _initialize(self):
        """初始化MCP会话"""
        full_url = self.base_url + self.endpoint_path
        
        init_payload = {
            "jsonrpc": "2.0",
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "stock-prediction-skill", "version": "1.0.0"}
            },
            "id": 0
        }
        
        http_ok = False
        http_error = False
        try:
            resp = requests.post(full_url, json=init_payload, timeout=10)
            if resp.ok:
                try:
                    data = resp.json()
                    if isinstance(data, dict) and 'error' in data:
                        http_error = True
                    else:
                        http_ok = True
                except Exception:
                    http_ok = True
            else:
                http_error = True
        except Exception:
            pass
        if not http_ok and not http_error:
            with self._responses_cond:
                self.responses.clear()
            start_len = 0
            deadline = time.monotonic() + 10
            with self._responses_cond:
                start_len = len(self.responses)
                while len(self.responses) == start_len:
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        break
                    self._responses_cond.wait(remaining)
            if not self.responses or len(self.responses) == start_len or 'error' in self.responses[-1]:
                raise Exception("❌ MCP初始化失败")
        if http_error:
            raise Exception("❌ MCP初始化失败")
        
        notif_payload = {"jsonrpc": "2.0", "method": "notifications/initialized"}
        requests.post(full_url, json=notif_payload)
        
        self.initialized = True

    def _parse_result_text_to_df(self, text, tool_name=None):
        if not isinstance(text, str) or not text.strip():
            raise Exception("❌ 无法解析查询结果")
        raw = text.strip()
        if raw.startswith("Error executing query:"):
            raise Exception(f"❌ SQL执行失败: {raw}")

        # Tool-specific parsing logic
        if tool_name == "security_lookup":
            try:
                data = json.loads(raw)
                if "hits" in data and "hits" in data["hits"]:
                    hits = data["hits"]["hits"]
                    rows = [h["_source"] for h in hits if "_source" in h]
                    return pd.DataFrame(rows)
                return pd.DataFrame()
            except Exception:
                # If JSON parsing fails, maybe fallback?
                pass
        b64_text = raw
        if "base64," in b64_text[:200]:
            b64_text = b64_text.split("base64,", 1)[1]
        b64_text = "".join(b64_text.split())

        decoded_bytes = None
        try:
            decoded_bytes = base64.b64decode(b64_text, validate=True)
        except Exception:
            try:
                decoded_bytes = base64.urlsafe_b64decode(b64_text)
            except Exception:
                decoded_bytes = None

        if decoded_bytes is not None:
            if decoded_bytes[:4] == b"PAR1":
                try:
                    return pd.read_parquet(BytesIO(decoded_bytes))
                except Exception:
                    try:
                        import fastparquet

                        pf = fastparquet.ParquetFile(BytesIO(decoded_bytes))
                        return pf.to_pandas()
                    except Exception as e:
                        raise Exception("❌ 解析Parquet失败，请在环境中安装 pyarrow 或 fastparquet") from e
            try:
                decoded_text = decoded_bytes.decode("utf-8")
                return pd.read_csv(StringIO(decoded_text), dtype=str)
            except Exception:
                pass

        return pd.read_csv(StringIO(raw), dtype=str)

    def _try_http_query(self, full_url, payload):
        # Extract tool name
        tool_name = payload.get("params", {}).get("name")
        
        try:
            resp = requests.post(full_url, json=payload, timeout=(10, 30))
        except Exception as e:
            return None, e
        if resp.status_code == 202:
            return None, None
        if not resp.ok:
            body = (resp.text or "").strip()
            if len(body) > 500:
                body = body[:500] + "..."
            return None, Exception(f"HTTP {resp.status_code}: {body}")
        if not resp.content:
            return None, None
        try:
            data = resp.json()
        except Exception as e:
            return None, None
        if not isinstance(data, dict):
            return None, None
        if "error" in data:
            raise Exception(f"❌ SQL错误: {data['error']}")
        if "result" in data and "content" in data["result"]:
            content = data["result"]["content"]
            if not content or "text" not in content[0] or not content[0]["text"]:
                raise Exception("❌ 无法解析查询结果")
            return self._parse_result_text_to_df(content[0]["text"], tool_name=tool_name), None
        return None, None

    def _wait_sse_result(self, timeout=10, request_id=None, start_index=0, tool_name=None):
        deadline = time.monotonic() + timeout
        result = None
        with self._responses_cond:
            while True:
                window = self.responses[start_index:]
                if request_id is not None:
                    for item in reversed(window):
                        if isinstance(item, dict) and item.get("id") == request_id:
                            result = item
                            break
                if result is None:
                    for item in reversed(window):
                        if isinstance(item, dict) and ("result" in item or "error" in item):
                            result = item
                            break
                if result is not None:
                    break
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    return None
                self._responses_cond.wait(remaining)
        if "error" in result:
            raise Exception(f"❌ SQL错误: {result['error']}")
        if "result" in result and "content" in result["result"]:
            content = result["result"]["content"]
            if not content or "text" not in content[0] or not content[0]["text"]:
                raise Exception("❌ 无法解析查询结果")
            return self._parse_result_text_to_df(content[0]["text"], tool_name=tool_name)
        return None

    def query(self, sql):
        """执行SQL查询"""
        if not self.initialized:
            raise Exception("❌ MCP未初始化,请先调用connect()")
        
        full_url = self.base_url + self.endpoint_path
        last_error = None
        tool_name = "execute_sql_v2"
        for attempt in range(3):
            request_id = int(time.time() * 1000) * 10 + attempt
            with self._responses_cond:
                start_index = len(self.responses)
            payload = {
                "jsonrpc": "2.0",
                "method": "tools/call",
                "params": {
                    "name": tool_name,
                    "arguments": {"query": sql}
                },
                "id": request_id
            }
            df, err = self._try_http_query(full_url, payload)
            if df is not None:
                return df
            if err is not None:
                last_error = err
            try:
                df = self._wait_sse_result(timeout=120, request_id=request_id, start_index=start_index, tool_name=tool_name)
            except Exception as e:
                msg = str(e)
                if msg.startswith("❌ SQL错误") or msg.startswith("❌ SQL执行失败"):
                    raise
                last_error = e
                df = None
            if df is None:
                last_error = Exception("❌ 查询超时")
            else:
                return df
            if attempt < 2:
                time.sleep(0.5 * (2 ** attempt) + random.random() * 0.3)
        if last_error:
            raise last_error
        raise Exception("❌ 查询失败")

    def lookup(self, keywords, limit=200):
        if not self.initialized:
            raise Exception("MCP not initialized")
        
        full_url = self.base_url + self.endpoint_path
        
        request_id = int(time.time() * 1000)
        tool_name = "security_lookup"
        with self._responses_cond:
            start_index = len(self.responses)
            
        payload = {
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": {"keywords": keywords, "limit": limit}
            },
            "id": request_id
        }
        
        # Reuse _try_http_query from parent
        # It will use our overridden _parse_result_text_to_df
        df, err = self._try_http_query(full_url, payload)
        
        if df is not None:
            return df
        
        if err is not None:
            raise err
            
        # Wait for SSE result
        return self._wait_sse_result(timeout=10, request_id=request_id, start_index=start_index, tool_name=tool_name)

def query_trading_days(mcp, dates, markets=None, include_flags=False):
    fields = "TradingDate, SecuMarket, IfTradingDay"
    if include_flags:
        fields += ", IfWeekEnd, IfMonthEnd, IfQuarterEnd, IfYearEnd"
    dates_in = ",".join(f"'{d}'" for d in dates)
    sql = f"""
    SELECT {fields}
    FROM qt_tradingdaynew
    WHERE DATE(TradingDate) IN ({dates_in})
    """
    if markets:
        markets_in = ",".join(str(m) for m in markets)
        sql += f" AND SecuMarket IN ({markets_in})"
    sql += "\n    ORDER BY TradingDate ASC, SecuMarket ASC\n    "
    df = mcp.query(sql)
    return df

def main():
    print("🔄 正在连接Finance Data MCP...")
    mcp = FinanceMCP()
    mcp.connect()
    print("✅ MCP连接成功")


if __name__ == "__main__":
    main()
