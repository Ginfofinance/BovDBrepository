# Codes — Example Scripts & Notebooks

Ready-to-run example scripts demonstrating how to use the **BovDB** dataset and the `bovdb` Python SDK for common research and visualization tasks.

---

## Prerequisites

1. Install the BovDB package with visualization extras:
   ```bash
   pip install -e ".[viz]"
   ```
2. Place the SQLite database at `DataBase/DataBase.db` (see [download instructions](../BovdbV2/README.md#-download-the-database)).

---

## Available Examples

| Script | Description | Dataset Version | Output |
|---|---|---|---|
| [`daily_candlesticks_chart.py`](daily_candlesticks_chart.py) | Daily candlestick chart with and without split-adjustment factor | V1+ | Matplotlib chart |
| [`annual_mean_and_standard_deviation_graph.py`](annual_mean_and_standard_deviation_graph.py) | Yearly mean price ± standard deviation, comparing nominal vs. adjusted | V1+ | Matplotlib chart |
| [`intraday_5min_candlestick.py`](intraday_5min_candlestick.py) | Interactive 5-minute intraday candlestick chart | V2+ (requires `price5`) | Plotly interactive chart |
| [`low_and_bottom.ipynb`](low_and_bottom.ipynb) | Top & bottom extrema detection on price series | V1+ | Jupyter Notebook |

---

## Usage

```bash
# Daily candlestick (with and without factor adjustment)
python Codes/daily_candlesticks_chart.py

# Annual mean and standard deviation
python Codes/annual_mean_and_standard_deviation_graph.py

# Intraday 5-minute candlestick (interactive Plotly)
python Codes/intraday_5min_candlestick.py

# Top & Bottom extrema detection (Jupyter)
jupyter notebook Codes/low_and_bottom.ipynb
```

---

## Extending

These scripts are meant as starting points. They use the `bovdb` SDK internally:

```python
from bovdb import get_connection, get_daily_prices, plot_candlestick

conn = get_connection()  # Safe read-only connection
df = get_daily_prices(conn, ticker="PETR4", adjusted=True)
plot_candlestick(df, ticker_name="PETR4")
conn.close()
```

For the full API reference, see [`src/bovdb/`](../src/bovdb/).
