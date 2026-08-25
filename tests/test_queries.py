"""
Functional tests for BovDB SQL queries and pandas extraction helpers.
"""

import pytest
import pandas as pd
import bovdb


def test_list_companies(conn):
    df = bovdb.list_companies(conn)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3
    assert "PETROLEO BRASILEIRO S.A. PETROBRAS" in df["name"].values
    assert "VALE S.A." in df["name"].values


def test_list_tickers(conn):
    df = bovdb.list_tickers(conn)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 4
    assert set(df["cd_ticker"].values) == {"PETR4", "PETR3", "VALE3", "ITUB4"}
    # Check that company metadata joined properly
    petr4_row = df[df["cd_ticker"] == "PETR4"].iloc[0]
    assert petr4_row["company_name"] == "PETROLEO BRASILEIRO S.A. PETROBRAS"


def test_get_daily_prices_by_ticker_string(conn):
    df = bovdb.get_daily_prices(conn, ticker="PETR4")
    assert len(df) == 3
    assert list(df["cd_ticker"].unique()) == ["PETR4"]
    assert "open" in df.columns
    assert "close" in df.columns
    assert "factor" in df.columns


def test_get_daily_prices_by_id(conn):
    df = bovdb.get_daily_prices(conn, ticker=101)
    assert len(df) == 3
    assert df.iloc[0]["id_ticker"] == 101


def test_get_daily_prices_date_filtering(conn):
    df = bovdb.get_daily_prices(conn, ticker="PETR4", start_date="2023-01-03", end_date="2023-01-03")
    assert len(df) == 1
    assert str(df.iloc[0]["date"].strftime("%Y-%m-%d")) == "2023-01-03"


def test_get_daily_prices_invalid_ticker_raises(conn):
    with pytest.raises(ValueError, match="Ticker symbol 'NONEXISTENT' not found"):
        bovdb.get_daily_prices(conn, ticker="NONEXISTENT")


def test_get_intraday_5min(conn):
    df = bovdb.get_intraday_5min(conn, ticker="PETR4", start_date="2024-06-26", end_date="2024-06-26")
    assert len(df) == 4
    assert "datetime" in df.columns
    assert df.iloc[0]["time"] == "10:00:00"
    assert df.iloc[-1]["time"] == "10:15:00"
