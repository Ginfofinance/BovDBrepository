"""
Database connection and path resolution for BovDB SQLite database.
"""

import os
import sqlite3
from pathlib import Path
from typing import Optional, Union


def resolve_database_path(custom_path: Optional[Union[str, Path]] = None) -> Path:
    """
    Resolves the absolute path to the BovDB SQLite database file.

    Search priority:
    1. Explicit custom_path argument
    2. BOVDB_PATH environment variable
    3. Standard relative project locations:
       - DataBase/DataBase.db
       - DataBase/Database_define.db
       - ../DataBase/DataBase.db
       - ../DataBase/Database_define.db
       - ../../DataBase/DataBase.db
    """
    if custom_path:
        p = Path(custom_path)
        if p.exists():
            return p.resolve()
        raise FileNotFoundError(f"Specified database path does not exist: {p}")

    env_path = os.getenv("BOVDB_PATH")
    if env_path:
        p = Path(env_path)
        if p.exists():
            return p.resolve()
        raise FileNotFoundError(f"Path in BOVDB_PATH environment variable does not exist: {p}")

    search_candidates = [
        Path("DataBase/DataBase.db"),
        Path("DataBase/Database_define.db"),
        Path("../DataBase/DataBase.db"),
        Path("../DataBase/Database_define.db"),
        Path("../../DataBase/DataBase.db"),
        Path("../../DataBase/Database_define.db"),
    ]

    for candidate in search_candidates:
        if candidate.exists():
            return candidate.resolve()

    # If not found, default to standard local repo path and raise informative error
    default_path = Path("DataBase/DataBase.db").resolve()
    return default_path


def get_connection(
    db_path: Optional[Union[str, Path]] = None,
    check_exists: bool = False
) -> sqlite3.Connection:
    """
    Creates and returns a connection to the BovDB SQLite database.

    Args:
        db_path: Optional explicit path to the database file.
        check_exists: If True, raises FileNotFoundError if the file doesn't exist.

    Returns:
        sqlite3.Connection: Open SQLite connection object.
    """
    resolved_path = resolve_database_path(db_path)
    if check_exists and not resolved_path.exists():
        raise FileNotFoundError(
            f"BovDB database not found at '{resolved_path}'. "
            "Please download and extract DataBase.db into the DataBase/ folder."
        )
    return sqlite3.connect(str(resolved_path))
