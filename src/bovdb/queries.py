"""
Query functions to extract and transform data from BovDB SQLite database.
"""

import sqlite3
from typing import Optional, Union
import pandas as pd


def list_companies(conn: sqlite3.Connection) -> pd.DataFrame:
    """
    Returns a DataFrame listing all companies in the database.
    """
    query = "SELECT id_company, name, sector, subsector, segment FROM company ORDER BY id_company"
    return pd.read_sql_query(query, conn)


def list_tickers(conn: sqlite3.Connection) -> pd.DataFrame:
    """
    Returns a DataFrame listing all tickers with their associated company metadata.
    """
    query = """
    SELECT 
        t.id_ticker,
        t.cd_ticker,
        t.type,
        c.id_company,
        c.name as company_name,
        c.sector,
        c.subsector,
        c.segment
    FROM ticker t
    LEFT JOIN company c ON t.id_company = c.id_company
    ORDER BY t.cd_ticker
    """
    return pd.read_sql_query(query, conn)


def get_ticker_id(conn: sqlite3.Connection, cd_ticker: str) -> Optional[int]:
    """
    Looks up the numeric id_ticker for a given ticker code (e.g. 'PETR4' -> 107).
    """
    query = "SELECT id_ticker FROM ticker WHERE UPPER(cd_ticker) = ? LIMIT 1"
    cur = conn.cursor()
    cur.execute(query, (cd_ticker.upper(),))
    row = cur.fetchone()
    return row[0] if row else None


def get_daily_prices(
    conn: sqlite3.Connection,
    ticker: Union[str, int],
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    adjusted: bool = False,
) -> pd.DataFrame:
    """
    Fetches daily price data for a specific ticker.

    Args:
        conn: SQLite connection.
        ticker: Either numeric id_ticker (e.g. 107) or ticker symbol (e.g. 'PETR4').
        start_date: Start date string in 'YYYY-MM-DD' format (inclusive).
        end_date: End date string in 'YYYY-MM-DD' format (inclusive).
        adjusted: If True, divides open, high, low, close by factor.

    Returns:
        pd.DataFrame: Formatted DataFrame with date index and OHLCV columns.
    """
    if isinstance(ticker, str):
        ticker_id = get_ticker_id(conn, ticker)
        if ticker_id is None:
            raise ValueError(f"Ticker symbol '{ticker}' not found in database.")
    else:
        ticker_id = ticker

    conditions = ["p.id_ticker = ?"]
    params = [ticker_id]

    if start_date:
        conditions.append("p.date >= ?")
        params.append(start_date)
    if end_date:
        conditions.append("p.date <= ?")
        params.append(end_date)

    where_clause = " AND ".join(conditions)
    query = f"""
    SELECT 
        p.id_ticker,
        t.cd_ticker,
        p.date,
        p.open,
        p.high,
        p.low,
        p.close,
        p.volume,
        p.trades,
        p.factor
    FROM price p
    JOIN ticker t ON p.id_ticker = t.id_ticker
    WHERE {where_clause}
    ORDER BY p.date ASC
    """
    df = pd.read_sql_query(query, conn, params=params)

    if not df.empty:
        df["date"] = pd.to_datetime(df["date"])
        if adjusted:
            df["open"] = df["open"] / df["factor"]
            df["high"] = df["high"] / df["factor"]
            df["low"] = df["low"] / df["factor"]
            df["close"] = df["close"] / df["factor"]

    return df


def get_adjusted_daily_prices(
    conn: sqlite3.Connection,
    ticker: Union[str, int],
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> pd.DataFrame:
    """
    Convenience wrapper returning factor-adjusted daily prices.
    """
    return get_daily_prices(conn, ticker, start_date=start_date, end_date=end_date, adjusted=True)


def get_intraday_5min(
    conn: sqlite3.Connection,
    ticker: Union[str, int],
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> pd.DataFrame:
    """
    Fetches 5-minute intraday price data from the price5 table.

    Args:
        conn: SQLite connection.
        ticker: Either numeric id_ticker or ticker symbol.
        start_date: Start date in 'YYYY-MM-DD' format.
        end_date: End date in 'YYYY-MM-DD' format.

    Returns:
        pd.DataFrame: DataFrame with datetime column and 5-min OHLCV bars.
    """
    if isinstance(ticker, str):
        ticker_id = get_ticker_id(conn, ticker)
        if ticker_id is None:
            raise ValueError(f"Ticker symbol '{ticker}' not found in database.")
    else:
        ticker_id = ticker

    conditions = ["p.id_ticker = ?"]
    params = [ticker_id]

    if start_date:
        conditions.append("p.date >= ?")
        params.append(start_date)
    if end_date:
        conditions.append("p.date <= ?")
        params.append(end_date)

    where_clause = " AND ".join(conditions)
    query = f"""
    SELECT 
        p.id_ticker,
        t.cd_ticker,
        p.date,
        p.time,
        p.open,
        p.high,
        p.low,
        p.close,
        p.volume,
        p.trades
    FROM price5 p
    JOIN ticker t ON p.id_ticker = t.id_ticker
    WHERE {where_clause}
    ORDER BY p.date ASC, p.time ASC
    """
    df = pd.read_sql_query(query, conn, params=params)

    if not df.empty:
        df["datetime"] = pd.to_datetime(df["date"] + " " + df["time"])

    return df
