# 🐍 BovDB Python API Reference

The `bovdb` package provides typed, zero-overhead helper functions to query SQLite data into pandas DataFrames and generate interactive visualizations.

---

## 1. Connection Management

### `bovdb.get_connection(db_path=None, check_exists=False)`
Returns an active `sqlite3.Connection` instance. Automatically scans standard paths:
- `DataBase/DataBase.db`
- `DataBase/Database_define.db`
- Value of `BOVDB_PATH` environment variable.

```python
import bovdb
conn = bovdb.get_connection()
```

---

## 2. Querying Data

### `bovdb.list_companies(conn)`
Returns a DataFrame containing all companies and their B3 sectoral classifications.

### `bovdb.list_tickers(conn)`
Returns a DataFrame with all tickers and linked company metadata.

### `bovdb.get_daily_prices(conn, ticker, start_date=None, end_date=None, adjusted=False)`
Fetches daily OHLCV prices for a specific ticker symbol (e.g. `'PETR4'`) or numeric ID.
- `adjusted=True`: Divides OHLC by `factor` column.

### `bovdb.get_intraday_5min(conn, ticker, start_date=None, end_date=None)`
Fetches 5-minute intraday quotes from the `price5` table with an indexed datetime column.

---

## 3. Visualization Helpers

### `bovdb.plot_candlestick(df, ticker_name="ASSET", with_factor=False, save_path=None, show=True)`
Generates professional daily candlestick charts using `mplfinance`.

### `bovdb.plot_intraday_5min(df, day=None, ticker_name="ASSET", save_html=None, show=True)`
Generates interactive 5-minute intraday candlestick charts using `plotly`.

### `bovdb.plot_annual_stats(df, ticker_name="VALE3", start_year=1995, end_year=2024, save_path=None, show=True)`
Generates yearly mean prices with standard deviation error bars comparing nominal and factor-adjusted prices.
