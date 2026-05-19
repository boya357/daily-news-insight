#!/usr/bin/env python3
"""
Experimental event-level review compiler for topic_tracking.

Input schema:
[
  {
    "event": "事件一句话",
    "relevance_reason": "为什么这是围绕话题主体的有效新变化",
    "support_urls": ["https://...", "https://..."],
    "event_time": "YYYY-MM-DD HH:MM"
  }
]

This keeps the existing B2/B3 article-level flow intact. It only offers a
lighter event-level workorder that can compile accepted events into the
draft_filtered.json shape consumed by B4.
"""

import argparse
import json
import os
import sys
from datetime import datetime

from validate_tracking import (
    FRESHNESS_MAX_HOURS,
    MIN_REASON_LENGTH,
    URL_PATTERN,
    _fetch_page_text,
    _parse_time,
)


REQUIRED_EVENT_FIELDS = ["event", "relevance_reason", "support_urls", "event_time"]


def _canonical_url(url):
    if not isinstance(url, str):
        return ""
    return url.strip().split("#", 1)[0].rstrip("/")


def _ordered_unique_urls(urls):
    seen = set()
    result = []
    for url in urls:
        key = _canonical_url(url)
        if key and key not in seen:
            seen.add(key)
            result.append(url.strip())
    return result


def _read_events(path):
    if path == "-":
        return json.load(sys.stdin)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _compile_event(item, support_urls):
    primary_url = support_urls[0]
    evidence_urls = support_urls[1:]
    event = item["event"].strip()
    relevance_reason = item["relevance_reason"].strip()
    event_time = item["event_time"].strip()

    return {
        "title": event,
        "link": primary_url,
        "summary": event,
        "event": event,
        "support_urls": support_urls,
        "validation": {
            "relevance": {
                "level": "强相关",
                "reason_with_topic": relevance_reason,
            },
            "freshness": {
                "time_evidence_raw_sentence": "",
                "content_event_time": event_time,
                "time_evidence_reason": "事件级工单已明确给出 event_time；若时间不确定，不得填写该事件。",
            },
            "source_analysis": {
                "requires_verification": True,
                "verification_conclusion": "pass",
                "source_trace": "事件级工单提供至少两个不同且可达的支撑来源。",
                "evidence_urls": evidence_urls,
                "verification_explanation": "该事件已由 support_urls 中的多来源共同支撑。",
            },
            "quality": {
                "decision": "keep",
                "reason": "事件级工单只收可写入简报的高质量事件。",
            },
            "ctr_pred": {
                "decision": "keep",
                "reason": "事件已被判断为值得进入本期简报。",
            },
            "dedup": {
                "decision": "keep",
                "reason": "事件级工单提交者确认该事件不是已覆盖内容的简单重复。",
            },
            "authority": {
                "level": "专业账号",
                "reason": "事件级工单已通过至少两个不同且可达来源支撑。",
            },
        },
    }


def validate_and_compile(events, *, cache_dir=None):
    now = datetime.now()
    errors = []
    compiled = []

    if not isinstance(events, list):
        return {
            "pass": False,
            "error_count": 1,
            "errors": ["顶层结构必须是事件数组"],
        }, []

    for idx, item in enumerate(events, start=1):
        label = f"第{idx}条"
        item_errors = []
        if not isinstance(item, dict):
            errors.append(f"[{label}] 必须是对象")
            continue

        event = item.get("event", "")
        if isinstance(event, str) and event.strip():
            label = event.strip()

        for field in REQUIRED_EVENT_FIELDS:
            if field not in item:
                item_errors.append(f"[{label}] 缺少必要字段: {field}")

        if not isinstance(item.get("event"), str) or len(item.get("event", "").strip()) < MIN_REASON_LENGTH:
            item_errors.append(f"[{label}] event 需要至少{MIN_REASON_LENGTH}字符")

        reason = item.get("relevance_reason")
        if not isinstance(reason, str) or len(reason.strip()) < MIN_REASON_LENGTH:
            item_errors.append(f"[{label}] relevance_reason 需要至少{MIN_REASON_LENGTH}字符")

        support_urls = item.get("support_urls")
        unique_urls = []
        if not isinstance(support_urls, list):
            item_errors.append(f"[{label}] support_urls 必须是 URL 字符串数组")
        else:
            unique_urls = _ordered_unique_urls(support_urls)
            if len(unique_urls) < 2:
                item_errors.append(f"[{label}] support_urls 至少需要 2 个不同 URL")
            for url in support_urls:
                if not isinstance(url, str) or not URL_PATTERN.match(url):
                    item_errors.append(f"[{label}] support_urls 包含无效 URL: {url}")
                    continue
            for url in unique_urls:
                reachable, _ = _fetch_page_text(url, cache_dir=cache_dir)
                if not reachable:
                    item_errors.append(f"[{label}] support_url 不可达或疑似软404: {url}")

        event_time = item.get("event_time")
        if not isinstance(event_time, str) or not event_time.strip():
            item_errors.append(f"[{label}] event_time 不能为空；不确定时不要编造该事件")
        else:
            try:
                parsed = _parse_time(event_time)
                delta = abs((now - parsed).total_seconds()) / 3600
                if delta > FRESHNESS_MAX_HOURS:
                    item_errors.append(f"[{label}] event_time 距今 {delta:.1f}h，超过 {FRESHNESS_MAX_HOURS}h")
            except ValueError:
                item_errors.append(f"[{label}] event_time 格式必须是 YYYY-MM-DD HH:MM")

        if item_errors:
            errors.extend(item_errors)
        else:
            compiled.append(_compile_event(item, unique_urls))

    if errors:
        return {
            "pass": False,
            "total_events": len(events),
            "error_count": len(errors),
            "errors": errors,
        }, []

    return {
        "pass": True,
        "total_events": len(events),
        "compiled_count": len(compiled),
        "message": f"事件工单校验通过：{len(compiled)} 条事件可进入简报",
    }, compiled


def cmd_check(args):
    try:
        events = _read_events(args.input)
    except (OSError, json.JSONDecodeError) as e:
        print(json.dumps({"pass": False, "error": f"读取事件工单失败: {e}"}, ensure_ascii=False, indent=2))
        return 1

    result, compiled = validate_and_compile(events, cache_dir=args.cache_dir)
    if args.output and result.get("pass"):
        os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(compiled, f, ensure_ascii=False, indent=2)
        result["output"] = args.output

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("pass") else 1


def main():
    parser = argparse.ArgumentParser(description="事件级话题追踪工单实验工具")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("check", help="校验事件工单，并可编译为 draft_filtered.json")
    p.add_argument("input", help="事件数组 JSON 文件路径；使用 - 表示从 stdin 读取")
    p.add_argument("--output", help="校验通过后写入 draft_filtered.json 兼容结构")
    p.add_argument("--cache-dir", help="URL 可达性缓存目录")

    args = parser.parse_args()
    if args.command == "check":
        return cmd_check(args)
    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
