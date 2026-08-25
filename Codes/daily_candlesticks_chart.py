"""
Daily Candlesticks Chart Generator (with and without factor adjustment) for BovDB.

Allows visual inspection of price adjustments (stock splits / corporate events).
"""

import sys
from pathlib import Path

# Add project root and src to sys.path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "src"))
sys.path.insert(0, str(project_root))

from bovdb import get_connection, get_daily_prices, plot_candlestick


def main():
    ticker = "PETR4"
    start_date = "2005-08-24"
    end_date = "2005-09-10"

    print("\n" + "=" * 70)
    print(" BovDB Daily Candlestick Chart Generator")
    print("=" * 70)
    print(f"Loading data for {ticker} between {start_date} and {end_date}...")

    conn = get_connection()
    try:
        df = get_daily_prices(conn, ticker=ticker, start_date=start_date, end_date=end_date)
        if df.empty:
            print(f"No data found for {ticker} in range {start_date} to {end_date}.")
            print("Please ensure DataBase/DataBase.db exists and is extracted properly.")
            return

        print("\nSelect visualization mode:")
        print("1. Daily Candlesticks (without factor adjustment)")
        print("2. Daily Candlesticks (with factor adjustment)")
        print("3. Export both to PDF")
        print("0. Exit")

        choice = input("\nEnter choice [0-3]: ").strip()

        if choice == "1":
            plot_candlestick(df, ticker_name=ticker, with_factor=False, show=True)
        elif choice == "2":
            plot_candlestick(df, ticker_name=ticker, with_factor=True, show=True)
        elif choice == "3":
            plot_candlestick(df, ticker_name=ticker, with_factor=False, save_path="daily_candlesticks_chart.pdf", show=False)
            plot_candlestick(df, ticker_name=ticker, with_factor=True, save_path="daily_candlesticks_chart_factor.pdf", show=False)
            print("Exported: daily_candlesticks_chart.pdf and daily_candlesticks_chart_factor.pdf")
        else:
            print("Exiting.")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
