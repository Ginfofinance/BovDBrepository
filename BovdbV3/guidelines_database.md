# Guidelines for BovDB Version 3.0 Database

This document outlines instructions for downloading, extracting, verifying, and configuring the **BovDB Version 3.0** SQLite database.

---

## 1. Downloading the Database

Due to GitHub's file size limits on binary repositories, the complete SQLite database is distributed in a compressed archive (`.rar` or `.zip`).

1. Open `BovdbV3/link_database.txt` to find the current active download links.
2. Download the compressed file to your local machine.

---

## 2. Extracting and Positioning

1. Extract the compressed file using your preferred archive tool (e.g. WinRAR, 7-Zip, or `unrar`/`unzip` on Linux):
   ```bash
   # Linux / macOS (example):
   unrar x Database_define.rar DataBase/
   ```
2. Ensure the resulting SQLite database file is located at:
   ```text
   BovDbV3repository/DataBase/DataBase.db
   ```
   *(Alternatively, `DataBase/Database_define.db` is also recognized automatically by the `bovdb` module)*.

---

## 3. Configuring the Database Path

The `bovdb` helper module automatically scans the following locations:
1. Custom path specified in environment variable `BOVDB_PATH` (or `.env` file).
2. `DataBase/DataBase.db`
3. `DataBase/Database_define.db`
4. `../DataBase/DataBase.db` (when running from within the `Codes/` folder).

---

## 4. Verifying Installation

Run the quick verification check using Python:

```bash
python -c "from bovdb import get_connection, list_tickers; conn = get_connection(); print(list_tickers(conn).head()); conn.close()"
```
