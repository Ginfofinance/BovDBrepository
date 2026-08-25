# bovdb — Python SDK

The `bovdb` package provides a safe, modular Python interface for querying and visualizing the BovDB stock quotes database.

---

## Installation

```bash
# From the repository root:
pip install -e "."          # Core only (pandas, numpy)
pip install -e ".[viz]"     # + matplotlib, mplfinance, plotly
pip install -e ".[analysis]"  # + scipy
pip install -e ".[dev]"     # + pytest, build, twine
pip install -e ".[all]"     # Everything
```

---

## Modules

| Module | Description |
|---|---|
| [`connection.py`](connection.py) | Database path resolution and SQLite connection management. Opens in **strict read-only mode** by default (`file:?mode=ro`) to prevent accidental database corruption or empty DB creation. |
| [`queries.py`](queries.py) | Data extraction functions returning `pandas.DataFrame`. Supports daily prices, intraday 5-min bars, adjusted prices, and metadata queries. |
| [`visualization.py`](visualization.py) | Chart rendering functions for candlestick charts (mplfinance), interactive intraday plots (Plotly), and annual statistics graphs. Requires `bovdb[viz]` extras. |

---

## Public API

### Connection

| Function | Description |
|---|---|
| `resolve_database_path(custom_path=None)` | Resolves the SQLite database path. Priority: `custom_path` > `BOVDB_PATH` env var > `DataBase/DataBase.db`. Raises `FileNotFoundError` if not found. |
| `get_connection(db_path=None, read_only=True)` | Returns a `sqlite3.Connection`. Read-only by default via URI mode. |

### Queries

| Function | Description |
|---|---|
| `list_companies(conn)` | Lists all companies with sector metadata. |
| `list_tickers(conn)` | Lists all tickers with associated company info. |
| `get_ticker_id(conn, cd_ticker)` | Resolves a ticker symbol (e.g., `"PETR4"`) to its `id_ticker`. |
| `get_daily_prices(conn, ticker, start_date, end_date, adjusted)` | Fetches daily OHLCV data. Set `adjusted=True` for split-adjusted prices. |
| `get_adjusted_daily_prices(conn, ticker, start_date, end_date)` | Convenience wrapper for adjusted daily prices (divides by `factor`). |
| `get_intraday_5min(conn, ticker, start_date, end_date)` | Fetches 5-minute intraday OHLCV bars from the `price5` table. |

### Visualization

| Function | Description |
|---|---|
| `plot_candlestick(df, ticker_name, with_factor, save_path, show)` | Renders a daily candlestick chart using mplfinance. |
| `plot_intraday_5min(df, day, ticker_name, save_path, show)` | Renders an interactive 5-minute intraday candlestick chart using Plotly. |
| `plot_annual_stats(df, ticker_name, save_path, show)` | Renders annual mean ± standard deviation comparison chart. |

---

## Quick Example

```python
import bovdb

conn = bovdb.get_connection()  # Safe read-only connection

# List all available companies
companies = bovdb.list_companies(conn)
print(companies.head())

# Fetch split-adjusted daily prices for Petrobras
df = bovdb.get_daily_prices(conn, ticker="PETR4", start_date="2023-01-01", adjusted=True)
bovdb.plot_candlestick(df, ticker_name="PETR4 (Adjusted)")

conn.close()
```

---

## Version Metadata

```python
import bovdb

bovdb.__version__                # "0.1.0" (SDK version)
bovdb.DEFAULT_DATASET_VERSION    # "2.0" (latest published dataset)
bovdb.SUPPORTED_DATASET_VERSIONS # ("1.0", "2.0", "3.0-dev")
```
