"""
BovDB: Stock Quotes Dataset for Machine Learning on Brazilian Equities (B3).
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

__version__ = "3.0.0"
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
]
