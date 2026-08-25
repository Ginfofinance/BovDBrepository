# BovDB Local Database Directory

This directory is the local destination for the uncompressed **BovDB SQLite database** file.

### How to use:
1. Download the compressed database archive (`Database_define.rar` or `.zip`) following the links in [`BovdbV3/link_database.txt`](../BovdbV3/link_database.txt).
2. Extract the file into this folder as `DataBase.db` (or `Database_define.db`).
3. The expected structure is:
   ```text
   DataBase/
   ├── .gitkeep
   ├── README.md
   └── DataBase.db       <-- Your uncompressed SQLite database
   ```

*Note: The `.gitignore` file is configured to ignore all `.db`, `.sqlite`, `.rar`, and `.zip` files in this directory to prevent large binaries from being committed to Git.*
