# BovDB Version 1.0 (1995 – 2020)

This directory contains the original historical dataset files published in **BovDB v1.0** (SBBD 2021).

## Dataset Scope
- **Time Range**: 1995 to 2020.
- **Coverage**: All equities traded on the Brazilian Stock Exchange (B3).
- **Resolution**: Daily historical OHLCV quotes with adjustment factors.

## Included Archive Formats
- `DataBase_CSV.zip`: CSV exports of all tables.
- `DataBase_JSON.zip`: JSON structured records.
- `DataBase.db.zip` / `DataBase.zip`: Original SQLite database file.

## Schema
The database contains tables:
- `company`: Information on listed companies.
- `ticker`: Asset tickers mapped to companies.
- `price`: Daily OHLCV quotes with corporate adjustment factor.
