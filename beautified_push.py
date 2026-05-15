#!/usr/bin/env python3
"""
美化推送脚本 - 生成摘要并推送到企业微信
遵循推送全流程规范V2
"""

import sys
import os
import re
import requests
from datetime import datetime

# 添加项目根目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# 导入日志系统和工具函数
from enable_logging import setup_logger
from report_utils import extract_summary, validate_report

# 初始化日志
logger = setup_logger('beautified_push', 'logs/beautified_push.log')


def load_markdown_file(file_path: str) -> str:
    """
    加载Markdown文件内容
    
    Args:
        file_path: Markdown文件路径
        
    Returns:
        文件内容字符串
    """
    try:
        if not os.path.exists(file_path):
            logger.error(f"文件不存在: {file_path}")
            return ''
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        logger.info(f"成功加载文件: {file_path}, 大小: {len(content)}字节")
        return content
        
    except Exception as e:
        logger.error(f"加载文件失败: {str(e)}", exc_info=True)
        return ''


def extract_index_data(content: str) -> str:
    """
    提取指数数据
    
    Args:
        content: Markdown内容
        
    Returns:
        格式化的指数数据字符串
    """
    try:
        # 匹配指数表格
        table_pattern = r'## 指数数据\s*\n\|.*?\|\s*\n\|.*?\|\s*\n((\|.*?\|\s*\n)+)'
        match = re.search(table_pattern, content, re.DOTALL)
        
        if not match:
            logger.warning("未找到指数数据表格")
            return ''
        
        table_content = match.group(1)
        rows = re.findall(r'\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|', table_content)
        
        if not rows:
            logger.warning("指数表格无数据行")
            return ''
        
        # 格式化输出
        formatted = "📊 指数数据:\n"
        for row in rows:
            if row[0] == '指数' or not row[0].strip():
                continue
            formatted += f"• {row[0]}: {row[1]} ({row[2]})\n"
        
        logger.info(f"成功提取指数数据，共{len(rows)-1}个指数")
        return formatted
        
    except Exception as e:
        logger.error(f"提取指数数据失败: {str(e)}", exc_info=True)
        return ''


def extract_main_themes(content: str) -> str:
    """
    提取三大主线
    
    Args:
        content: Markdown内容
        
    Returns:
        格式化的主线字符串
    """
    try:
        # 匹配三大主线
        theme_pattern = r'## 三大主线\s*\n((•.*?\n)+)'
        match = re.search(theme_pattern, content, re.DOTALL)
        
        if not match:
            logger.warning("未找到三大主线")
            return ''
        
        theme_content = match.group(1)
        themes = re.findall(r'•\s*(.*?)(?=\n•|\n$)', theme_content)
        
        if not themes:
            logger.warning("三大主线无内容")
            return ''
        
        # 格式化输出
        formatted = "🚀 三大主线:\n"
        for i, theme in enumerate(themes[:3], 1):
            formatted += f"{i}. {theme}\n"
        
        logger.info(f"成功提取三大主线，共{len(themes)}条")
        return formatted
        
    except Exception as e:
        logger.error(f"提取三大主线失败: {str(e)}", exc_info=True)
        return ''


def extract_limit_up_stocks(content: str) -> str:
    """
    提取连板梯队
    
    Args:
        content: Markdown内容
        
    Returns:
        格式化的连板梯队字符串
    """
    try:
        # 匹配连板梯队表格
        table_pattern = r'## 连板梯队\s*\n\|.*?\|\s*\n\|.*?\|\s*\n((\|.*?\|\s*\n)+)'
        match = re.search(table_pattern, content, re.DOTALL)
        
        if not match:
            logger.warning("未找到连板梯队表格")
            return ''
        
        table_content = match.group(1)
        rows = re.findall(r'\|\s*([^|]+)\s*\|\s*(\d+)连板\s*\|\s*(.*?)\s*\|', table_content)
        
        if not rows:
            logger.warning("连板梯队表格无数据行")
            return ''
        
        # 按连板数排序
        rows.sort(key=lambda x: int(x[1]), reverse=True)
        
        # 格式化输出
        formatted = "🏆 连板梯队:\n"
        for row in rows[:5]:  # 最多显示5只
            formatted += f"• {row[0]}: {row[1]}连板 ({row[2]})\n"
        
        logger.info(f"成功提取连板梯队，共{len(rows)}只股票")
        return formatted
        
    except Exception as e:
        logger.error(f"提取连板梯队失败: {str(e)}", exc_info=True)
        return ''


def extract_risk_warnings(content: str) -> str:
    """
    提取风险提示
    
    Args:
        content: Markdown内容
        
    Returns:
        格式化的风险提示字符串
    """
    try:
        # 匹配风险提示
        risk_pattern = r'## ⚠️ 风险提示\s*\n((•.*?\n)+)'
        match = re.search(risk_pattern, content, re.DOTALL)
        
        if not match:
            logger.warning("未找到风险提示")
            return ''
        
        risk_content = match.group(1)
        risks = re.findall(r'•\s*(.*?)(?=\n•|\n$)', risk_content)
        
        if not risks:
            logger.warning("风险提示无内容")
            return ''
        
        # 格式化输出
        formatted = "⚠️ 风险提示:\n"
        for risk in risks[:3]:  # 最多显示3条
            formatted += f"• {risk}\n"
        
        logger.info(f"成功提取风险提示，共{len(risks)}条")
        return formatted
        
    except Exception as e:
        logger.error(f"提取风险提示失败: {str(e)}", exc_info=True)
        return ''


def generate_github_link(file_path: str) -> str:
    """
    生成GitHub Pages链接
    
    Args:
        file_path: 原始报告文件路径
        
    Returns:
        GitHub链接字符串
    """
    try:
        # 从文件名提取日期
        file_name = os.path.basename(file_path)
        date_match = re.search(r'(\d{8})', file_name)
        
        if not date_match:
            logger.warning("无法从文件名提取日期")
            return ''
        
        date_str = date_match.group(1)
        
        # 判断报告类型
        if '盘中快报' in file_name:
            report_type = 'intraday'
        elif '盘后速递' in file_name:
            report_type = 'aftermarket'
        elif '每日新闻' in file_name:
            report_type = 'daily'
        else:
            report_type = 'other'
        
        # 生成链接
        link = f"https://boya357.github.io/daily-news-insight/{report_type}/{date_str}"
        logger.info(f"生成GitHub链接: {link}")
        return link
        
    except Exception as e:
        logger.error(f"生成GitHub链接失败: {str(e)}", exc_info=True)
        return ''


def push_to_wechat_work(content: str, webhook_url: str = None) -> bool:
    """
    推送到企业微信
    
    Args:
        content: 推送内容
        webhook_url: 企业微信Webhook URL，留空则从环境变量获取
        
    Returns:
        是否推送成功
    """
    try:
        if not content.strip():
            logger.error("推送内容为空，跳过推送")
            return False
        
        if not webhook_url:
            webhook_url = os.getenv('WECHAT_WORK_WEBHOOK')
            if not webhook_url:
                logger.error("企业微信Webhook URL未设置")
                return False
        
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
            logger.info("成功推送到企业微信")
            return True
        else:
            logger.error(f"企业微信推送失败: {result.get('errmsg', '未知错误')}")
            return False
            
    except requests.exceptions.RequestException as e:
        logger.error(f"推送请求失败: {str(e)}", exc_info=True)
        return False
    except Exception as e:
        logger.error(f"推送失败: {str(e)}", exc_info=True)
        return False


def main(file_path: str):
    """
    主函数
    
    Args:
        file_path: 报告文件路径
    """
    logger.info(f"开始处理推送任务: {file_path}")
    
    # 1. 加载文件内容
    content = load_markdown_file(file_path)
    if not content:
        logger.error("文件内容为空，终止推送")
        return
    
    # 2. 验证报告内容
    is_valid, errors = validate_report(content)
    if not is_valid:
        logger.warning(f"报告验证不通过，但仍尝试推送: {errors}")
    
    # 3. 提取各部分内容
    index_data = extract_index_data(content)
    main_themes = extract_main_themes(content)
    limit_up_stocks = extract_limit_up_stocks(content)
    risk_warnings = extract_risk_warnings(content)
    github_link = generate_github_link(file_path)
    
    # 4. 生成推送内容
    # 判断报告类型并生成对应标题
    if '盘中快报' in content or '盘中快报' in file_path:
        push_title = "📰 【盘中快报 · 午间版】"
    elif '盘后速递' in content or '盘后速递' in file_path:
        push_title = "📊 【盘后速递】"
    else:
        push_title = "📰 【每日新闻洞察】"
    
    push_content = f"""
{push_title}
━━━━━━━━━━━━━━━━━━━
"""
    
    if index_data:
        push_content += f"\n{index_data}"
    if main_themes:
        push_content += f"\n{main_themes}"
    if limit_up_stocks:
        push_content += f"\n{limit_up_stocks}"
    if risk_warnings:
        push_content += f"\n{risk_warnings}"
    if github_link:
        push_content += f"\n📖 查看完整报告: {github_link}"
    
    # 产业链总览引导语
    GITHUB_TOTAL_LINK = "https://boya357.github.io/daily-news-insight/"
    push_content += f"\n\n> 产业链研究报告总览: {GITHUB_TOTAL_LINK} 💡 点击上方链接可查看所有产业链研究报告，包括：DeepSeek/PCB/CPO/航天/氦气铜箔等追踪题材的最新分析"
    
    push_content = push_content.strip()
    
    if not push_content:
        logger.error("推送内容生成失败，无有效信息")
        return
    
    logger.info(f"生成推送内容，长度: {len(push_content)}字符")
    logger.debug(f"推送内容: {push_content}")
    
    # 5. 推送至企业微信
    success = push_to_wechat_work(push_content)
    
    if success:
        logger.info("推送任务完成")
    else:
        logger.error("推送任务失败")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("用法: python beautified_push.py <报告文件路径>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    main(file_path)