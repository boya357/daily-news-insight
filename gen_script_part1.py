#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""盘后速递生成脚本 - 2026-11-23"""
import sys, os
sys.path.insert(0, "v3")
os.chdir("/root/daily-news-insight")

from v3.generators.aftermarket import AftermarketGenerator
from v3.components.layout import Section

gen = AftermarketGenerator(date_str="20261123", subtitle="2026.11.23 · 盘后速递")
