"""
BovDB: Python Toolkit for Stock Quotes Dataset on Brazilian Equities (B3).
"""

from .connection import get_connection, resolve_database_path
from .queries import (
    list_companies,
    list_tickers,
    get_daily_prices,
    get_intraday_5min,
    get_adjusted_daily_prices,
)
from .visualization import (
    plot_candlestick,
    plot_intraday_5min,
    plot_annual_stats,
)

# Semantic SDK package version
__version__ = "0.1.0"

# Dataset version metadata
DEFAULT_DATASET_VERSION = "3.0"
SUPPORTED_DATASET_VERSIONS = ("1.0", "2.0", "3.0")

__all__ = [
    "get_connection",
    "resolve_database_path",
    "list_companies",
    "list_tickers",
    "get_daily_prices",
    "get_intraday_5min",
    "get_adjusted_daily_prices",
    "plot_candlestick",
    "plot_intraday_5min",
    "plot_annual_stats",
    "__version__",
    "DEFAULT_DATASET_VERSION",
    "SUPPORTED_DATASET_VERSIONS",
]
