"""
Annual Mean and Standard Deviation Graph (with and without factor) for BovDB.

Calculates the yearly mean price and standard deviation for a given company/ticker,
comparing nominal prices against factor-adjusted prices.
"""

import sys
from pathlib import Path

# Add project root and src to sys.path to enable local imports
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "src"))
sys.path.insert(0, str(project_root))

from bovdb import get_connection, get_daily_prices, plot_annual_stats


def main():
    ticker = "VALE3"
    start_year = 1995
    end_year = 2024
    output_pdf = "annual_mean_and_standard_deviation_graph.pdf"

    print(f"Connecting to BovDB database and loading data for {ticker} ({start_year}-{end_year})...")
    conn = get_connection()
    try:
        df = get_daily_prices(conn, ticker=ticker, start_date=f"{start_year}-01-01", end_date=f"{end_year}-12-31")
        if df.empty:
            print(f"Warning: No data returned for {ticker}. Ensure DataBase/DataBase.db is present.")
            return

        print(f"Generating annual statistics chart for {ticker}...")
        plot_annual_stats(
            df=df,
            ticker_name=ticker,
            start_year=start_year,
            end_year=end_year,
            save_path=output_pdf,
            show=False
        )
        print(f"Chart saved successfully to '{output_pdf}'.")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
