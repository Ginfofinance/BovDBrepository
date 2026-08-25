"""
Functional tests for BovDB corporate action adjustment factors (splits, inplits, bonuses).
"""

import bovdb


def test_adjusted_daily_prices_formula(conn):
    # PETR4 has factor = 2.0 in the test fixture
    df_raw = bovdb.get_daily_prices(conn, ticker="PETR4", adjusted=False)
    df_adj = bovdb.get_daily_prices(conn, ticker="PETR4", adjusted=True)

    assert len(df_raw) == len(df_adj)

    # Verify that Price_adjusted == Price_nominal / factor for all OHLC fields
    for col in ["open", "high", "low", "close"]:
        calculated = df_raw[col] / df_raw["factor"]
        assert (calculated == df_adj[col]).all()


def test_adjusted_daily_prices_exact_values(conn):
    # Nominal close on 2023-01-02 is 21.0, factor is 2.0 -> Adjusted close should be 10.5
    df_adj = bovdb.get_adjusted_daily_prices(conn, ticker="PETR4", start_date="2023-01-02", end_date="2023-01-02")
    assert df_adj.iloc[0]["close"] == 10.5
    assert df_adj.iloc[0]["open"] == 10.0


def test_factor_one_unaffected(conn):
    # VALE3 has factor = 1.0 in the test fixture -> adjusted == raw
    df_raw = bovdb.get_daily_prices(conn, ticker="VALE3", adjusted=False)
    df_adj = bovdb.get_daily_prices(conn, ticker="VALE3", adjusted=True)
    assert (df_raw["close"] == df_adj["close"]).all()
