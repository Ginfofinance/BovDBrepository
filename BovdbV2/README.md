# BovDB Version 2.0 — Dataset for Intraday Analysis of B3 Stock Prices

[![DOI](https://img.shields.io/badge/DOI-10.7910%2FDVN%2FTMB4IG-blue.svg)](https://doi.org/10.7910/DVN/TMB4IG)

> **Souza, A. S., Lucca, G., Borges, E. N., Cardoso, F. C., Dalmazo, B. L., & Berri, R. (2024).**
> *Dataset for Intraday Analysis of B3 stock prices.* Harvard Dataverse.
> DOI: [10.7910/DVN/TMB4IG](https://doi.org/10.7910/DVN/TMB4IG)

---

## Overview

**BovDB v2.0** is the officially published version of the BovDB dataset, extending the original V1 (SBBD 2021) with **4 additional years of daily data** and a brand-new **high-frequency 5-minute intraday table (`price5`)**, enabling research in algorithmic trading, microstructure analysis, and intraday pattern detection.

---

## 🔽 Download the Database

### Option 1 — Harvard Dataverse (Recommended)

The official, citable, and permanently archived version is hosted on the Harvard Dataverse:

1. Go to **<https://doi.org/10.7910/DVN/TMB4IG>**
2. Click **"Access Dataset"** → **"Download"** on the desired file(s).
3. Extract the SQLite database file (`DataBase.db`).
4. Place it at `DataBase/DataBase.db` (relative to the repository root).

### Option 2 — Dropbox Mirror

An alternative mirror is available on Dropbox. See the step-by-step guide in [`guidelines_database_dropbox.pdf`](guidelines_database_dropbox.pdf) or follow these quick steps:

1. Open the link in [`link_database.txt`](link_database.txt):
   ```
   https://www.dropbox.com/scl/fi/sris4tnltenf0twm20vt2/Database_define.rar?rlkey=0dnjx3xn7efdigc1neibe4kee&st=att3x9re&dl=0
   ```
2. Download `Database_define.rar`.
3. Extract with [7-Zip](https://www.7-zip.org/) or WinRAR.
4. Place the extracted `DataBase.db` at `DataBase/DataBase.db`.

---

## 🆕 What's New in V2 (compared to V1)

| Feature | V1 (SBBD 2021) | V2 (Harvard Dataverse 2024) |
|---|---|---|
| **Time Range** | 1995 – 2020 | 1995 – mid-2024 |
| **Daily Quotes** | ✅ OHLCV + adjustment factor | ✅ OHLCV + adjustment factor (4 more years) |
| **Intraday Data** | ❌ Not available | ✅ **5-minute bars** (`price5` table) — Jan to Jun 2024 |
| **Tables** | `company`, `ticker`, `price` | `company`, `ticker`, `price`, **`price5`** |
| **Distribution** | ZIP archives (CSV, JSON, SQLite) | SQLite via Harvard Dataverse (DOI) + Dropbox mirror |
| **Citable DOI** | ❌ | ✅ [10.7910/DVN/TMB4IG](https://doi.org/10.7910/DVN/TMB4IG) |

### Key Additions

- **`price5` table**: High-frequency 5-minute OHLCV candlestick bars for all B3 equities, timestamped in Brasília Time (BRT / UTC-3). Enables:
  - Intraday pattern detection and momentum analysis
  - High-frequency trading strategy backtesting
  - Microstructure research (spread, volatility clustering)
- **Extended daily coverage**: 4 additional years of daily OHLCV data (2021–2024), including COVID-19 market recovery and post-pandemic trends.
- **Permanent academic archival** via Harvard Dataverse with DOI for stable citation.

---

## Database Schema

| Table | Description | Primary Key |
|---|---|---|
| `company` | Listed companies on B3, sectoral classification | `id_company` |
| `ticker` | B3 tickers (ON, PN, UNT, BDRs) linked to companies | `id_ticker` |
| `price` | Daily OHLCV quotes with cumulative split/bonus `factor` | `(id_ticker, date)` |
| `price5` | 5-minute intraday OHLCV candlestick bars | `(id_ticker, date, time)` |

### Price Adjustment Formula

Prices in the `price` table are stored in **nominal terms**. To compute split-adjusted prices:

$$\text{Price}_{\text{adjusted}}(t) = \frac{\text{Price}_{\text{nominal}}(t)}{\text{factor}(t)}$$

---

## Files in this Directory

| File | Description |
|---|---|
| [`link_database.txt`](link_database.txt) | Dropbox download link for `Database_define.rar` |
| [`guidelines_database_dropbox.pdf`](guidelines_database_dropbox.pdf) | Step-by-step visual guide for downloading from Dropbox |
| [`manifest.json`](manifest.json) | Structured metadata (tables, format, distribution) |
| [`checksums.sha256`](checksums.sha256) | SHA-256 integrity hashes for verification |

---

## Citation

```bibtex
@data{DVN/TMB4IG_2024,
  author    = {Souza, Andrey S. and Lucca, Giancarlo and Borges, Eduardo N. and Cardoso, Fabian C. and Dalmazo, Bruno L. and Berri, Rafael},
  publisher = {Harvard Dataverse},
  title     = {{Dataset for Intraday Analysis of B3 stock prices}},
  year      = {2024},
  version   = {V1},
  doi       = {10.7910/DVN/TMB4IG},
  url       = {https://doi.org/10.7910/DVN/TMB4IG}
}
```

---

## License

This dataset is licensed under [Creative Commons Attribution-NonCommercial 4.0 International](../LICENSE.md) (CC BY-NC 4.0).
