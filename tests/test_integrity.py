"""
Integrity and schema validation tests for BovDB tables and relationships.
"""


def test_schema_tables_exist(conn):
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = {row[0] for row in cur.fetchall()}
    expected_tables = {"company", "ticker", "price", "price5"}
    assert expected_tables.issubset(tables)


def test_foreign_key_ticker_to_company(conn):
    cur = conn.cursor()
    # Check that all tickers point to existing companies
    cur.execute("""
    SELECT t.id_ticker, t.cd_ticker 
    FROM ticker t 
    LEFT JOIN company c ON t.id_company = c.id_company 
    WHERE c.id_company IS NULL
    """)
    orphaned_tickers = cur.fetchall()
    assert len(orphaned_tickers) == 0


def test_no_negative_prices_or_factors(conn):
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM price WHERE open < 0 OR high < 0 OR low < 0 OR close < 0 OR factor <= 0")
    invalid_rows = cur.fetchone()[0]
    assert invalid_rows == 0
