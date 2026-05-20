#!/usr/bin/env python3
"""企业微信简化推送脚本"""

import sys
import json
import urllib.request
import urllib.parse

def send_to_wecom(title, url, webhook_url=None):
    """发送消息到企业微信机器人"""
    if not webhook_url:
        # 默认使用环境变量或配置文件中的webhook
        webhook_url = os.environ.get('WECOM_WEBHOOK', '')
    
    if not webhook_url:
        print("⚠️ 未配置企业微信Webhook，消息跳过推送")
        print(f"📄 内容: {title}")
        print(f"🔗 链接: {url}")
        return False
    
    data = {
        "msgtype": "news",
        "news": {
            "articles": [
                {
                    "title": title,
                    "url": url
                }
            ]
        }
    }
    
    try:
        req = urllib.request.Request(
            webhook_url,
            data=json.dumps(data).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode('utf-8'))
            if result.get('errcode') == 0:
                print(f"✅ 企业微信推送成功")
                return True
            else:
                print(f"❌ 推送失败: {result}")
                return False
    except Exception as e:
        print(f"❌ 推送异常: {e}")
        return False

if __name__ == '__main__':
    import os
    if len(sys.argv) < 3:
        print("用法: python3 simple_push.py <标题> <URL> [webhook_url]")
        sys.exit(1)
    
    title = sys.argv[1]
    url = sys.argv[2]
    webhook = sys.argv[3] if len(sys.argv) > 3 else None
    
    send_to_wecom(title, url, webhook)
