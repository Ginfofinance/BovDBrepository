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
       - ../../DataBase/Database_define.db

    Raises:
        FileNotFoundError: If no valid database file exists at any candidate location.
    """
    if custom_path:
        p = Path(custom_path)
        if p.exists() and p.is_file():
            return p.resolve()
        raise FileNotFoundError(f"Specified database path does not exist: {p}")

    env_path = os.getenv("BOVDB_PATH")
    if env_path:
        p = Path(env_path)
        if p.exists() and p.is_file():
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
        if candidate.exists() and candidate.is_file():
            return candidate.resolve()

    checked_paths = [str(c.resolve()) for c in search_candidates[:2]]
    raise FileNotFoundError(
        "BovDB SQLite database file not found. "
        f"Checked default paths: {checked_paths}. "
        "Please download and extract DataBase.db into the DataBase/ folder, "
        "or set the BOVDB_PATH environment variable."
    )


def get_connection(
    db_path: Optional[Union[str, Path]] = None,
    read_only: bool = True,
) -> sqlite3.Connection:
    """
    Creates and returns a connection to the BovDB SQLite database.

    By default, connections are opened in read-only mode via URI ('?mode=ro')
    to prevent accidental file creation or modifications to scientific data.

    Args:
        db_path: Optional explicit path to the database file.
        read_only: If True (default), opens database in strict read-only mode.

    Returns:
        sqlite3.Connection: Open SQLite connection object.

    Raises:
        FileNotFoundError: If the database file is not found.
    """
    resolved_path = resolve_database_path(db_path)

    if read_only:
        # Convert path to URI format for sqlite3 read-only mode
        uri_path = f"file:{resolved_path.as_posix()}?mode=ro"
        return sqlite3.connect(uri_path, uri=True)

    return sqlite3.connect(str(resolved_path))
