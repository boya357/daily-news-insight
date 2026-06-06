"""
V3.0 报告生成器集合
所有类型报告的专用生成器都在这里
"""

from .deep_dive import DeepDiveGenerator
from .list_page import ListPageGenerator
from .daily import DailyReportGenerator
from .intraday import IntradayGenerator
from .aftermarket import AftermarketGenerator
from .weekly_review import WeeklyReviewGenerator
from .s_level_catalyst import SLevelCatalystGenerator
from .weekly_outlook import WeeklyOutlookGenerator
from .weekend_express import WeekendExpressGenerator
from .tomorrow_catalyst import TomorrowCatalystGenerator
from .monthly import MonthlyReportGenerator

__all__ = [
    'DeepDiveGenerator',
    'ListPageGenerator',
    'DailyReportGenerator',
    'IntradayGenerator',
    'AftermarketGenerator',
    'WeeklyReviewGenerator',
    'SLevelCatalystGenerator',
    'WeeklyOutlookGenerator',
    'WeekendExpressGenerator',
    'TomorrowCatalystGenerator',
    'MonthlyReportGenerator',
]
