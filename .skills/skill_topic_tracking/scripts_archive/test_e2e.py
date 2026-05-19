#!/usr/bin/env python3
"""
topic_tracking_v3 全流程端到端测试

测试场景：
1. validate_tracking.py 各种边界情况
2. 状态机流程模拟（Setup S1→S4 → Briefing B1→B10）
3. 直接进入 Briefing 流程
4. 从任意步骤恢复
5. 门控校验流程（B5 pass/fail/retry）
6. 留痕文件完整性检查
7. 话题追踪目录产出检查
"""

import json
import os
import sys
import uuid
import shutil
import subprocess
from datetime import datetime

# ===== 配置 =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(BASE_DIR, "validate_tracking.py")
TEST_ROOT = "/tmp/test_topic_tracking_e2e"
SESSIONS_DIR = os.path.join(TEST_ROOT, ".topic_tracking", "sessions")
TRACKING_DIR = os.path.join(TEST_ROOT, "话题追踪", "黄金价格")

# 测试计数
passed = 0
failed = 0
total = 0


def test(name, condition, detail=""):
    global passed, failed, total
    total += 1
    if condition:
        passed += 1
        print(f"  ✅ {name}")
    else:
        failed += 1
        print(f"  ❌ {name}" + (f" — {detail}" if detail else ""))


def run_validate(filepath):
    """运行验证脚本，返回 (exit_code, parsed_json)"""
    result = subprocess.run(
        [sys.executable, SCRIPT_PATH, filepath],
        capture_output=True, text=True
    )
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        data = {"raw_output": result.stdout, "raw_stderr": result.stderr}
    return result.returncode, data


def write_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def make_valid_article(title="测试文章", link="https://example.com"):
    return {
        "title": title,
        "link": link,
        "summary": "这是一篇关于测试的文章摘要，包含关键信息",
        "validation": {
            "relevance": "直接对应话题需求，包含核心数据和分析",
            "freshness": "2026-04-24 09:15 - 今日最新发布，时效性强",
            "quality": "包含具体数据、分析深度高、信息完整准确",
            "ctr_pred": "重大事件，对行业格局影响大，用户关注度高",
            "dedup": "首次覆盖，历史记忆中无相关记录",
            "authority": "权威媒体发布，数据来源可信，符合用户需求"
        }
    }


# ===== 清理 =====
if os.path.exists(TEST_ROOT):
    shutil.rmtree(TEST_ROOT)

# ============================================================
print("\n" + "=" * 60)
print("1. 验证脚本测试（validate_tracking.py）")
print("=" * 60)

# --- 1.1 正常通过 ---
print("\n[1.1] 正常通过")
path = os.path.join(TEST_ROOT, "v1_pass.json")
write_json(path, [make_valid_article("文章A"), make_valid_article("文章B", "https://b.com")])
code, data = run_validate(path)
test("退出码为 0", code == 0)
test("pass 为 true", data.get("pass") is True)
test("total_articles 为 2", data.get("total_articles") == 2)
test("有 dimensions_checked", len(data.get("dimensions_checked", [])) == 6)

# --- 1.2 缺少维度 ---
print("\n[1.2] 缺少维度")
path = os.path.join(TEST_ROOT, "v2_missing.json")
article = make_valid_article()
del article["validation"]["ctr_pred"]
del article["validation"]["dedup"]
write_json(path, [article])
code, data = run_validate(path)
test("退出码为 1", code == 1)
test("pass 为 false", data.get("pass") is False)
test("报告缺少 ctr_pred", any("ctr_pred" in e for e in data.get("errors", [])))
test("报告缺少 dedup", any("dedup" in e for e in data.get("errors", [])))

# --- 1.3 维度说明太短 ---
print("\n[1.3] 维度说明太短")
path = os.path.join(TEST_ROOT, "v3_short.json")
article = make_valid_article()
article["validation"]["relevance"] = "相关"
article["validation"]["freshness"] = "新"
write_json(path, [article])
code, data = run_validate(path)
test("退出码为 1", code == 1)
test("pass 为 false", data.get("pass") is False)
test("报告 relevance 太短", any("relevance" in e and "太短" in e for e in data.get("errors", [])))
test("报告 freshness 太短", any("freshness" in e and "太短" in e for e in data.get("errors", [])))
# 其他维度是正常的，应该不报错
test("error_count 为 2", data.get("error_count") == 2)

# --- 1.4 空数组 ---
print("\n[1.4] 空数组")
path = os.path.join(TEST_ROOT, "v4_empty.json")
write_json(path, [])
code, data = run_validate(path)
test("退出码为 1", code == 1)
test("报告空数组", "为空" in data.get("error", ""))

# --- 1.5 非法 JSON ---
print("\n[1.5] 非法 JSON")
path = os.path.join(TEST_ROOT, "v5_bad.json")
with open(path, "w") as f:
    f.write("{not valid json")
code, data = run_validate(path)
test("退出码为 1", code == 1)
test("报告解析失败", "解析失败" in data.get("error", ""))

# --- 1.6 缺少必要字段 ---
print("\n[1.6] 缺少必要字段")
path = os.path.join(TEST_ROOT, "v6_no_fields.json")
write_json(path, [{"validation": {"relevance": "test1234", "freshness": "test1234",
    "quality": "test1234", "ctr_pred": "test1234", "dedup": "test1234", "authority": "test1234"}}])
code, data = run_validate(path)
test("退出码为 1", code == 1)
test("报告缺少 title", any("title" in e for e in data.get("errors", [])))
test("报告缺少 link", any("link" in e for e in data.get("errors", [])))
test("报告缺少 summary", any("summary" in e for e in data.get("errors", [])))

# --- 1.7 文件不存在 ---
print("\n[1.7] 文件不存在")
code, data = run_validate("/tmp/nonexistent_file_xyz.json")
test("退出码为 1", code == 1)
test("报告文件不存在", "不存在" in data.get("error", ""))

# --- 1.8 无参数 ---
print("\n[1.8] 无参数")
result = subprocess.run([sys.executable, SCRIPT_PATH], capture_output=True, text=True)
test("退出码为 1", result.returncode == 1)
data = json.loads(result.stdout)
test("报告用法", "用法" in data.get("error", ""))

# --- 1.9 顶层非数组 ---
print("\n[1.9] 顶层非数组（dict）")
path = os.path.join(TEST_ROOT, "v9_dict.json")
write_json(path, {"title": "not an array"})
code, data = run_validate(path)
test("退出码为 1", code == 1)
test("报告非数组", "数组" in data.get("error", ""))

# --- 1.10 validation 不是 dict ---
print("\n[1.10] validation 不是 dict")
path = os.path.join(TEST_ROOT, "v10_val_str.json")
write_json(path, [{"title": "测试", "link": "https://a.com", "summary": "摘要", "validation": "不是对象"}])
code, data = run_validate(path)
test("退出码为 1", code == 1)
test("报告 validation 必须是对象", any("对象" in e for e in data.get("errors", [])))

# --- 1.11 维度为非字符串类型 ---
print("\n[1.11] 维度为非字符串类型")
path = os.path.join(TEST_ROOT, "v11_val_int.json")
article = make_valid_article()
article["validation"]["relevance"] = 85
write_json(path, [article])
code, data = run_validate(path)
test("退出码为 1", code == 1)
test("报告 relevance 非字符串", any("relevance" in e and "字符串" in e for e in data.get("errors", [])))

# --- 1.12 多篇文章混合错误 ---
print("\n[1.12] 多篇文章混合错误")
path = os.path.join(TEST_ROOT, "v12_mixed.json")
a1 = make_valid_article("好文章A")
a2 = make_valid_article("坏文章B")
del a2["validation"]["authority"]
a2["validation"]["quality"] = "差"
a3 = make_valid_article("好文章C")
write_json(path, [a1, a2, a3])
code, data = run_validate(path)
test("退出码为 1", code == 1)
test("total_articles 为 3", data.get("total_articles") == 3)
test("错误只在坏文章B", all("坏文章B" in e for e in data.get("errors", [])))
test("error_count 为 2", data.get("error_count") == 2)

# ============================================================
print("\n" + "=" * 60)
print("2. 状态机流程：Setup (S1→S4) → Briefing (B1→B10)")
print("=" * 60)

token = str(uuid.uuid4())
session_dir = os.path.join(SESSIONS_DIR, token)
os.makedirs(session_dir, exist_ok=True)

# 初始化 .state.json
state = {
    "token": token,
    "flow": "setup",
    "current_step": "S1",
    "topic": None,
    "tracking_dir": None,
    "completed_steps": [],
    "created_at": datetime.now().isoformat()
}
state_path = os.path.join(session_dir, ".state.json")
write_json(state_path, state)
test("创建 session 目录", os.path.isdir(session_dir))
test(".state.json 初始化", os.path.isfile(state_path))

# --- S1 探索话题 ---
print("\n[S1] 探索话题")
state = read_json(state_path)
test("当前步骤为 S1", state["current_step"] == "S1")
test("flow 为 setup", state["flow"] == "setup")

s1_trace = {
    "step": "S1", "timestamp": datetime.now().isoformat(),
    "input": {"topic": "黄金价格", "queries": ["黄金价格 最新", "黄金行情 走势"]},
    "output": {"total_results": 15, "identified_directions": ["国际金价", "央行购金", "美联储政策"]}
}
write_json(os.path.join(session_dir, "S1_exploration.json"), s1_trace)

state["current_step"] = "S2"
state["topic"] = "黄金价格"
state["completed_steps"].append("S1")
write_json(state_path, state)
test("留痕文件写入", os.path.isfile(os.path.join(session_dir, "S1_exploration.json")))
test("状态推进到 S2", read_json(state_path)["current_step"] == "S2")

# --- S2 用户确认 ---
print("\n[S2] 与用户确认")
s2_trace = {
    "step": "S2", "timestamp": datetime.now().isoformat(),
    "input": {"proposed_directions": ["国际金价", "央行购金", "美联储政策"]},
    "output": {
        "confirmed_directions": ["国际金价", "美联储政策"],
        "frequency": "DAILY",
        "storage_root": TEST_ROOT + "/话题追踪",
        "tracking_dir": TRACKING_DIR,
        "user_preferences": {"focus": "关注行情数据"}
    }
}
write_json(os.path.join(session_dir, "S2_confirmation.json"), s2_trace)

state["current_step"] = "S3"
state["tracking_dir"] = TRACKING_DIR
state["completed_steps"].append("S2")
write_json(state_path, state)
test("留痕文件写入", os.path.isfile(os.path.join(session_dir, "S2_confirmation.json")))
test("状态推进到 S3", read_json(state_path)["current_step"] == "S3")
test("tracking_dir 已设置", read_json(state_path)["tracking_dir"] == TRACKING_DIR)

# --- S3 创建日程 ---
print("\n[S3] 创建日程")
s3_trace = {
    "step": "S3", "timestamp": datetime.now().isoformat(),
    "input": {"topic": "黄金价格", "frequency": "DAILY"},
    "output": {
        "calendar_id": "cal-mock-12345",
        "summary": "话题追踪：黄金价格",
        "description": "【话题追踪任务 - 请使用 topic_tracking_v3 技能执行】\n\n## 话题\n黄金价格\n...",
        "dtstart": "202604250900",
        "rrule": {"freq": "DAILY", "interval": 1}
    }
}
write_json(os.path.join(session_dir, "S3_calendar.json"), s3_trace)

state["current_step"] = "S4"
state["completed_steps"].append("S3")
write_json(state_path, state)
test("留痕文件写入", os.path.isfile(os.path.join(session_dir, "S3_calendar.json")))
test("状态推进到 S4", read_json(state_path)["current_step"] == "S4")

# --- S4 切换到 Briefing ---
print("\n[S4] 切换到 Briefing 流程")
state["flow"] = "briefing"
state["current_step"] = "B1"
state["completed_steps"].append("S4")
write_json(state_path, state)
state = read_json(state_path)
test("flow 切换为 briefing", state["flow"] == "briefing")
test("current_step 切换为 B1", state["current_step"] == "B1")
test("completed_steps 包含 S1-S4", set(["S1", "S2", "S3", "S4"]).issubset(set(state["completed_steps"])))

# --- B1→B10 完整流程 ---
briefing_steps = [
    ("B1", "B1_task_context.json", {
        "input": {"trigger_type": "calendar"},
        "output": {"topic": "黄金价格", "directions": ["国际金价", "美联储政策"], "tracking_dir": TRACKING_DIR}
    }),
    ("B2", "B2_memory.json", {
        "input": {"memory_queries": ["黄金价格 追踪简报 摘要"]},
        "output": {"has_history": False, "tracking_history": {}, "user_habits": {}}
    }),
    ("B3", "B3_search_results.json", {
        "input": {"queries": ["黄金价格 最新行情", "美联储 黄金"], "freshness": 1},
        "output": {"total_results": 18, "retry_needed": False}
    }),
    ("B4", "B4_filtered.json", {
        "input": {"total_candidates": 18},
        "output": {"passed_count": 6, "rejected_count": 12, "deep_read_targets": ["url1", "url2"]}
    }),
]

for step_id, trace_file, trace_data in briefing_steps:
    print(f"\n[{step_id}] 执行中...")
    next_step = f"B{int(step_id[1:]) + 1}"
    trace = {"step": step_id, "timestamp": datetime.now().isoformat(), **trace_data}
    write_json(os.path.join(session_dir, trace_file), trace)
    state["current_step"] = next_step
    state["completed_steps"].append(step_id)
    write_json(state_path, state)
    test(f"留痕 {trace_file} 写入", os.path.isfile(os.path.join(session_dir, trace_file)))
    test(f"状态推进到 {next_step}", read_json(state_path)["current_step"] == next_step)

# --- B5 门控步骤 ---
print("\n[B5] 门控步骤 — 验证 validation.json")

# 先写一个不完整的 validation.json
os.makedirs(TRACKING_DIR, exist_ok=True)
today = datetime.now().strftime("%Y-%m-%d")
val_path = os.path.join(TRACKING_DIR, f"{today}_validation.json")

bad_article = make_valid_article("金价回调报道")
del bad_article["validation"]["dedup"]  # 故意缺少一个维度
write_json(val_path, [bad_article])

code, data = run_validate(val_path)
test("首次校验失败（缺 dedup）", code == 1 and data.get("pass") is False)
test("报告缺少 dedup", any("dedup" in e for e in data.get("errors", [])))

# 修复后重新写入
good_articles = [
    make_valid_article("金价回调报道", "https://wallstreetcn.com/articles/123"),
    make_valid_article("央行增持黄金", "https://reuters.com/gold-123"),
]
write_json(val_path, good_articles)

code, data = run_validate(val_path)
test("修复后校验通过", code == 0 and data.get("pass") is True)
test("验证 2 篇文章", data.get("total_articles") == 2)

# 写入 B5 留痕
b5_trace = {
    "step": "B5", "timestamp": datetime.now().isoformat(),
    "input": {"articles_count": 2, "validation_file_path": val_path},
    "output": {"validation_result": data, "retry_count": 1, "errors_fixed": ["补充 dedup 维度"]}
}
write_json(os.path.join(session_dir, "B5_validation.json"), b5_trace)
state["current_step"] = "B6"
state["completed_steps"].append("B5")
write_json(state_path, state)
test("B5 留痕写入", os.path.isfile(os.path.join(session_dir, "B5_validation.json")))
test("状态推进到 B6（仅校验通过后）", read_json(state_path)["current_step"] == "B6")

# --- B6→B10 ---
remaining_steps = [
    ("B6", "B6_deep_read.json", {
        "input": {"target_urls": ["url1", "url2"]},
        "output": {"has_new_content": True, "articles_read": [{"url": "url1", "key_data": ["金价 4692"]}]}
    }),
    ("B7", "B7_briefing_draft.json", {
        "input": {"articles_used": 6, "directions_covered": ["国际金价", "美联储政策"]},
        "output": {"title": f"今日黄金行情速览（{today[5:7]}-{today[8:10]}）：", "references_count": 5}
    }),
    ("B8", "B8_output.json", {
        "input": {"tracking_dir": TRACKING_DIR},
        "output": {"briefing_path": os.path.join(TRACKING_DIR, f"{today}.md"),
                   "validation_path": val_path, "is_append": False}
    }),
    ("B9", "B9_summary.json", {
        "input": {},
        "output": {"key_data": {"现货黄金": "4692 美元/盎司"}, "key_events": ["金价回调"]}
    }),
]

for step_id, trace_file, trace_data in remaining_steps:
    print(f"\n[{step_id}] 执行中...")
    next_step = f"B{int(step_id[1:]) + 1}"
    trace = {"step": step_id, "timestamp": datetime.now().isoformat(), **trace_data}
    write_json(os.path.join(session_dir, trace_file), trace)
    state["current_step"] = next_step
    state["completed_steps"].append(step_id)
    write_json(state_path, state)
    test(f"留痕 {trace_file} 写入", os.path.isfile(os.path.join(session_dir, trace_file)))
    test(f"状态推进到 {next_step}", read_json(state_path)["current_step"] == next_step)

# B8 额外：写入简报文件
briefing_md = f"**今日黄金行情速览（{today[5:7]}-{today[8:10]}）：**\n\n测试简报内容\n"
briefing_path = os.path.join(TRACKING_DIR, f"{today}.md")
with open(briefing_path, "w", encoding="utf-8") as f:
    f.write(briefing_md)
test("简报 .md 已写入", os.path.isfile(briefing_path))
test("validation.json 在同目录", os.path.isfile(val_path))

# B10 最后一步
print("\n[B10] 口语总结")
spoken = "今天黄金整体回调，从 4750 跌到 4692 附近。主要受美伊僵局影响。"
spoken_path = os.path.join(session_dir, "B10_spoken.txt")
with open(spoken_path, "w", encoding="utf-8") as f:
    f.write(spoken)
state["current_step"] = "DONE"
state["completed_steps"].append("B10")
write_json(state_path, state)
test("B10 留痕写入", os.path.isfile(spoken_path))
test("状态推进到 DONE", read_json(state_path)["current_step"] == "DONE")

# ============================================================
print("\n" + "=" * 60)
print("3. 直接进入 Briefing 流程（日程触发）")
print("=" * 60)

token2 = str(uuid.uuid4())
session_dir2 = os.path.join(SESSIONS_DIR, token2)
os.makedirs(session_dir2, exist_ok=True)

state2 = {
    "token": token2,
    "flow": "briefing",
    "current_step": "B1",
    "topic": "黄金价格",
    "tracking_dir": TRACKING_DIR,
    "completed_steps": [],
    "created_at": datetime.now().isoformat()
}
write_json(os.path.join(session_dir2, ".state.json"), state2)
test("Briefing 直接创建成功", read_json(os.path.join(session_dir2, ".state.json"))["flow"] == "briefing")
test("从 B1 开始", read_json(os.path.join(session_dir2, ".state.json"))["current_step"] == "B1")

# ============================================================
print("\n" + "=" * 60)
print("4. 从任意步骤恢复")
print("=" * 60)

# 模拟在 B4 中断
token3 = str(uuid.uuid4())
session_dir3 = os.path.join(SESSIONS_DIR, token3)
os.makedirs(session_dir3, exist_ok=True)

state3 = {
    "token": token3,
    "flow": "briefing",
    "current_step": "B4",
    "topic": "AI 大模型",
    "tracking_dir": os.path.join(TEST_ROOT, "话题追踪", "AI大模型"),
    "completed_steps": ["B1", "B2", "B3"],
    "created_at": datetime.now().isoformat()
}
write_json(os.path.join(session_dir3, ".state.json"), state3)

# 模拟之前的留痕文件存在
for prev in ["B1_task_context.json", "B2_memory.json", "B3_search_results.json"]:
    write_json(os.path.join(session_dir3, prev), {"step": prev[:2], "timestamp": datetime.now().isoformat()})

state_recovered = read_json(os.path.join(session_dir3, ".state.json"))
test("恢复到 B4", state_recovered["current_step"] == "B4")
test("已完成 B1-B3", state_recovered["completed_steps"] == ["B1", "B2", "B3"])
test("前置留痕完整", all(
    os.path.isfile(os.path.join(session_dir3, f))
    for f in ["B1_task_context.json", "B2_memory.json", "B3_search_results.json"]
))
test("B4 留痕还不存在", not os.path.isfile(os.path.join(session_dir3, "B4_filtered.json")))

# 模拟在 S2 中断
token4 = str(uuid.uuid4())
session_dir4 = os.path.join(SESSIONS_DIR, token4)
os.makedirs(session_dir4, exist_ok=True)
state4 = {
    "token": token4, "flow": "setup", "current_step": "S2",
    "topic": "中美关系", "tracking_dir": None,
    "completed_steps": ["S1"], "created_at": datetime.now().isoformat()
}
write_json(os.path.join(session_dir4, ".state.json"), state4)
write_json(os.path.join(session_dir4, "S1_exploration.json"), {"step": "S1"})
test("Setup 中断恢复到 S2", read_json(os.path.join(session_dir4, ".state.json"))["current_step"] == "S2")
test("S1 留痕存在", os.path.isfile(os.path.join(session_dir4, "S1_exploration.json")))

# ============================================================
print("\n" + "=" * 60)
print("5. 完整性检查：Setup→Briefing 全流程留痕")
print("=" * 60)

# 检查第一个完整 session 的所有文件
expected_files = [
    ".state.json",
    "S1_exploration.json", "S2_confirmation.json", "S3_calendar.json",
    "B1_task_context.json", "B2_memory.json", "B3_search_results.json",
    "B4_filtered.json", "B5_validation.json", "B6_deep_read.json",
    "B7_briefing_draft.json", "B8_output.json", "B9_summary.json",
    "B10_spoken.txt",
]
for f in expected_files:
    test(f"存在 {f}", os.path.isfile(os.path.join(session_dir, f)))

# 检查最终状态
final_state = read_json(os.path.join(session_dir, ".state.json"))
test("最终状态为 DONE", final_state["current_step"] == "DONE")
test("flow 为 briefing", final_state["flow"] == "briefing")
all_steps = ["S1", "S2", "S3", "S4", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]
test("completed_steps 包含全部步骤", all(s in final_state["completed_steps"] for s in all_steps),
     f"缺少: {set(all_steps) - set(final_state['completed_steps'])}")

# 检查话题追踪目录产出
test(f"简报 {today}.md 存在", os.path.isfile(os.path.join(TRACKING_DIR, f"{today}.md")))
test(f"validation {today}_validation.json 存在", os.path.isfile(os.path.join(TRACKING_DIR, f"{today}_validation.json")))

# 检查 validation.json 校验仍然通过
code, data = run_validate(os.path.join(TRACKING_DIR, f"{today}_validation.json"))
test("最终 validation.json 校验通过", code == 0 and data.get("pass") is True)

# ============================================================
print("\n" + "=" * 60)
print("6. 多 session 并存")
print("=" * 60)

sessions = os.listdir(SESSIONS_DIR)
test(f"共 {len(sessions)} 个 session", len(sessions) == 4)
for sid in sessions:
    sp = os.path.join(SESSIONS_DIR, sid, ".state.json")
    test(f"session {sid[:8]}... 有 .state.json", os.path.isfile(sp))

# ============================================================
print("\n" + "=" * 60)
print("7. 同一天追加简报")
print("=" * 60)

# 模拟同一天第二次执行
existing_content = open(os.path.join(TRACKING_DIR, f"{today}.md"), "r", encoding="utf-8").read()
append_content = "\n---\n\n**今日黄金行情速览（更新 18:00）：**\n\n第二次推送内容\n"
with open(os.path.join(TRACKING_DIR, f"{today}.md"), "a", encoding="utf-8") as f:
    f.write(append_content)
updated_content = open(os.path.join(TRACKING_DIR, f"{today}.md"), "r", encoding="utf-8").read()
test("追加成功", "---" in updated_content)
test("两段简报都在", "测试简报内容" in updated_content and "第二次推送内容" in updated_content)

# ============================================================
# 汇总
print("\n" + "=" * 60)
print(f"测试结果：{passed}/{total} 通过，{failed} 失败")
print("=" * 60)

# 清理
shutil.rmtree(TEST_ROOT)

sys.exit(0 if failed == 0 else 1)
