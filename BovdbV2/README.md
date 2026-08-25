# BovDB Version 2.0 (1995 – 2024 + Intraday)

This directory contains metadata, official download links, and guidelines for **BovDB v2.0**.

## Dataset Scope
- **Time Range**: 1995 to mid-2024.
- **Coverage**: All equities traded on B3.
- **Resolution**: Daily OHLCV quotes + High-frequency 5-minute intraday bars (`price5`).

## Files in this Directory
- `link_database.txt`: Official DropBox download mirror for `Database_define.rar`.
- `guidelines_database_dropbox.pdf`: Original user guide for downloading and extracting the database from DropBox.

## Tables
- `company`: Listed companies and sectoral metadata.
- `ticker`: B3 tickers (ON, PN, UNT, BDRs).
- `price`: Daily OHLCV quotes with `factor`.
- `price5`: 5-minute intraday OHLCV candlestick quotes.
