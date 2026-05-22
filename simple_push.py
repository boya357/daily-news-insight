#!/usr/bin/env python3
"""
简单推送脚本 - 推送到企业微信
只用news卡片推送链接，不生成摘要
"""

import sys
import requests


def push_to_wechat_work(title: str, url: str) -> bool:
    """
    推送到企业微信 - news卡片格式
    
    Args:
        title: 报告标题
        url: 报告链接
        
    Returns:
        是否推送成功
    """
    try:
        webhook_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=e03b424c-69ae-4ea7-b099-3003d8f4dd52"
        
        payload = {
            "msgtype": "news",
            "news": {
                "articles": [
                    {
                        "title": title,
                        "description": "点击查看完整报告",
                        "url": url,
                        "picurl": ""
                    }
                ]
            }
        }
        
        response = requests.post(webhook_url, json=payload, timeout=10)
        response.raise_for_status()
        
        result = response.json()
        if result.get('errcode') == 0:
            print(f"✅ 成功推送{title}到企业微信")
            return True
        else:
            print(f"❌ 推送失败: {result}")
            return False
            
    except Exception as e:
        print(f"❌ 推送异常: {str(e)}")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: python3 simple_push.py <标题> <链接>")
        sys.exit(1)
    
    title = sys.argv[1]
    url = sys.argv[2]
    
    success = push_to_wechat_work(title, url)
    sys.exit(0 if success else 1)
