"""
Intraday 5-Minute Candlestick Chart (Plotly interactive) for BovDB price5 table.

Visualizes 5-minute price action for any ticker during intraday trading sessions.
"""

import sys
from pathlib import Path

# Add project root and src to sys.path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "src"))
sys.path.insert(0, str(project_root))

from bovdb import get_connection, get_intraday_5min, plot_intraday_5min


def main():
    ticker = "PETR4"
    start_date = "2024-06-26"
    end_date = "2024-06-26"

    print(f"Loading 5-minute intraday quotes for {ticker} on {start_date}...")
    conn = get_connection()
    try:
        df = get_intraday_5min(conn, ticker=ticker, start_date=start_date, end_date=end_date)
        if df.empty:
            print(f"No intraday quotes found for {ticker} in range {start_date} to {end_date}.")
            print("Note: The price5 table contains intraday data for recent periods.")
            return

        unique_days = df["date"].unique()
        print(f"Found trading sessions for days: {list(unique_days)}")

        for day in unique_days:
            print(f"Plotting 5-minute intraday candlestick chart for {day}...")
            plot_intraday_5min(df, day=day, ticker_name=ticker, show=True)

    finally:
        conn.close()


if __name__ == "__main__":
    main()
