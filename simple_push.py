#!/usr/bin/env python3
"""
简单推送脚本 - 推送到企业微信
"""

import sys
import os
import requests


def push_to_wechat_work(title: str, url: str) -> bool:
    """
    推送到企业微信
    
    Args:
        title: 报告标题
        url: 报告链接
        
    Returns:
        是否推送成功
    """
    try:
        webhook_url = os.getenv('WECHAT_WORK_WEBHOOK')
        if not webhook_url:
            print("企业微信Webhook URL未设置")
            return False
        
        content = f"""## 📊 {title}

**报告已生成并推送至GitHub Pages**

🔗 [点击查看完整报告]({url})

---
*由投资助手自动推送*
"""
        
        payload = {
            "msgtype": "markdown",
            "markdown": {
                "content": content
            }
        }
        
        response = requests.post(webhook_url, json=payload, timeout=10)
        response.raise_for_status()
        
        result = response.json()
        if result.get('errcode') == 0:
            print(f"成功推送{title}到企业微信")
            return True
        else:
            print(f"推送失败: {result}")
            return False
            
    except Exception as e:
        print(f"推送异常: {str(e)}")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: python3 simple_push.py <标题> <链接>")
        sys.exit(1)
    
    title = sys.argv[1]
    url = sys.argv[2]
    
    success = push_to_wechat_work(title, url)
    sys.exit(0 if success else 1)
