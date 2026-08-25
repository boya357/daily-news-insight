#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
盘后速递生成脚本 - 2026-08-25
使用 V3.0 AftermarketGenerator
"""
import sys
import os

sys.path.insert(0, '/root/daily-news-insight/v3')
os.chdir('/root/daily-news-insight')

from v3.generators.aftermarket import AftermarketGenerator

gen = AftermarketGenerator(
    date_str='20260825',
    subtitle='2026.08.25 · 盘后速递'
)
print('生成器初始化完成')
