"""
Pytest configuration and shared fixtures for BovDB functional tests.
"""

import sys
from pathlib import Path
import pytest

# Ensure repository root is on sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tests.fixtures.sample_generator import create_sample_database, SAMPLE_DB_PATH
import bovdb


@pytest.fixture(scope="session")
def sample_db():
    """Provides path to a guaranteed fresh sample test database."""
    db_path = create_sample_database(SAMPLE_DB_PATH)
    yield db_path


@pytest.fixture
def conn(sample_db):
    """Provides an open read-only sqlite3.Connection to sample.db."""
    connection = bovdb.get_connection(db_path=sample_db, read_only=True)
    yield connection
    connection.close()
