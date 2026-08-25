"""
Functional tests for BovDB database connection management and read-only enforcement.
"""

import sqlite3
import pytest
from pathlib import Path
import bovdb


def test_connection_read_only_default(sample_db):
    conn = bovdb.get_connection(db_path=sample_db)
    cur = conn.cursor()
    # Test reading succeeds
    cur.execute("SELECT COUNT(*) FROM company")
    count = cur.fetchone()[0]
    assert count == 3
    conn.close()


def test_connection_prevents_write_in_readonly(sample_db):
    conn = bovdb.get_connection(db_path=sample_db, read_only=True)
    cur = conn.cursor()
    with pytest.raises(sqlite3.OperationalError, match="readonly"):
        cur.execute("INSERT INTO company (id_company, name) VALUES (99, 'TEST CO')")
    conn.close()


def test_connection_missing_database_raises_filenotfound():
    with pytest.raises(FileNotFoundError, match="Specified database path does not exist"):
        bovdb.get_connection(db_path=Path("non_existent_dir/non_existent.db"))


def test_resolve_default_missing_raises_filenotfound(monkeypatch, tmp_path):
    # Set CWD to an empty directory to ensure default search fails cleanly
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("BOVDB_PATH", raising=False)
    with pytest.raises(FileNotFoundError, match="BovDB SQLite database file not found"):
        bovdb.get_connection()
