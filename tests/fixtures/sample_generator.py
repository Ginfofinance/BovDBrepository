"""
Generates minimal SQLite sample database for automated functional tests.
"""

import sqlite3
from pathlib import Path

FIXTURES_DIR = Path(__file__).resolve().parent
SAMPLE_DB_PATH = FIXTURES_DIR / "sample.db"


def create_sample_database(db_path: Path = SAMPLE_DB_PATH) -> Path:
    if db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(str(db_path))
    cur = conn.cursor()

    # 1. Company Table
    cur.execute("""
    CREATE TABLE company (
        id_company INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        sector TEXT,
        subsector TEXT,
        segment TEXT
    );
    """)

    cur.executemany("""
    INSERT INTO company (id_company, name, sector, subsector, segment) VALUES (?, ?, ?, ?, ?);
    """, [
        (1, "PETROLEO BRASILEIRO S.A. PETROBRAS", "Petróleo, Gás e Biocombustíveis", "Petróleo, Gás e Biocombustíveis", "Exploração, Refino e Distribuição"),
        (2, "VALE S.A.", "Materiais Básicos", "Mineração", "Minerais Metálicos"),
        (3, "ITAU UNIBANCO HOLDING S.A.", "Financeiro", "Intermediários Financeiros", "Bancos"),
    ])

    # 2. Ticker Table
    cur.execute("""
    CREATE TABLE ticker (
        id_ticker INTEGER PRIMARY KEY,
        cd_ticker TEXT NOT NULL UNIQUE,
        id_company INTEGER,
        type TEXT,
        FOREIGN KEY(id_company) REFERENCES company(id_company)
    );
    """)

    cur.executemany("""
    INSERT INTO ticker (id_ticker, cd_ticker, id_company, type) VALUES (?, ?, ?, ?);
    """, [
        (101, "PETR4", 1, "PN"),
        (102, "PETR3", 1, "ON"),
        (201, "VALE3", 2, "ON"),
        (301, "ITUB4", 3, "PN"),
    ])

    # 3. Price Table (Daily OHLCV + factor)
    cur.execute("""
    CREATE TABLE price (
        id_ticker INTEGER NOT NULL,
        date TEXT NOT NULL,
        open REAL NOT NULL,
        high REAL NOT NULL,
        low REAL NOT NULL,
        close REAL NOT NULL,
        volume REAL,
        trades INTEGER,
        factor REAL NOT NULL DEFAULT 1.0,
        PRIMARY KEY (id_ticker, date),
        FOREIGN KEY(id_ticker) REFERENCES ticker(id_ticker)
    );
    """)

    cur.executemany("""
    INSERT INTO price (id_ticker, date, open, high, low, close, volume, trades, factor) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, [
        (101, "2023-01-02", 20.0, 22.0, 19.5, 21.0, 50000000.0, 12000, 2.0),
        (101, "2023-01-03", 21.0, 23.0, 20.5, 22.0, 60000000.0, 14000, 2.0),
        (101, "2023-01-04", 22.0, 24.0, 21.5, 23.0, 55000000.0, 13000, 2.0),
        (201, "2023-01-02", 80.0, 85.0, 79.0, 84.0, 100000000.0, 25000, 1.0),
        (201, "2023-01-03", 84.0, 88.0, 83.0, 87.0, 120000000.0, 28000, 1.0),
    ])

    # 4. Price5 Table (5-minute intraday quotes)
    cur.execute("""
    CREATE TABLE price5 (
        id_ticker INTEGER NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        open REAL NOT NULL,
        high REAL NOT NULL,
        low REAL NOT NULL,
        close REAL NOT NULL,
        volume REAL,
        trades INTEGER,
        PRIMARY KEY (id_ticker, date, time),
        FOREIGN KEY(id_ticker) REFERENCES ticker(id_ticker)
    );
    """)

    cur.executemany("""
    INSERT INTO price5 (id_ticker, date, time, open, high, low, close, volume, trades) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, [
        (101, "2024-06-26", "10:00:00", 35.0, 35.5, 34.9, 35.2, 1000000.0, 250),
        (101, "2024-06-26", "10:05:00", 35.2, 35.8, 35.1, 35.7, 1200000.0, 310),
        (101, "2024-06-26", "10:10:00", 35.7, 36.0, 35.6, 35.9, 1500000.0, 420),
        (101, "2024-06-26", "10:15:00", 35.9, 36.1, 35.7, 35.8, 900000.0, 210),
    ])

    conn.commit()
    conn.close()
    return db_path


if __name__ == "__main__":
    create_sample_database()
    print(f"Sample test database generated at: {SAMPLE_DB_PATH}")
