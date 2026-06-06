"""
V3.0 Report Generation System
- Single data source for all components
- Content-driven, style-unified
- Zero-trust validation
"""

# Core - import carefully to avoid circular deps
from .core.report import Report

# Components
from .components.base import Component
from .components.layout import Navbar, Footer, Section, Card
from .components.data import DataCard, DataGrid, CompareTable, MetricsRow
from .components.charts import LineChart, BarChart, PieChart
from .components.special import RiskAlert, QuoteBlock, Timeline, ButtonGroup, CatalystTag

# Generators
from .generators.deep_dive import DeepDiveGenerator
from .generators.list_page import ListPageGenerator

# Validators
from .validators.structure import StructureValidator
from .validators.links import LinkValidator
from .validators.content import ContentValidator

__version__ = "3.0.0"
__author__ = "投资研究团队"
