# BovDB Version 3.0 (1995 – Present)

This directory contains metadata, official download links, and guidelines for **BovDB v3.0**.

## Dataset Scope
- **Time Range**: 1995 to Present.
- **Coverage**: All equities traded on B3.
- **Resolution**: Daily OHLCV quotes + 5-minute intraday bars (`price5`).
- **Features**: Unified modular Python SDK (`bovdb`), CI/CD automation, comprehensive data dictionary, and reproducible research workflows.

## Files in this Directory
- `link_database.txt`: Official download mirrors (DropBox, Google Drive, Zenodo/HuggingFace).
- `guidelines_database.md`: Step-by-step setup and extraction guide.

## Setup
1. Download the database archive from [`link_database.txt`](link_database.txt).
2. Extract `DataBase.db` into the `DataBase/` directory at the repository root.
3. Use the Python `bovdb` module to query and visualize data.
