# BovDB Version 1.0 — Stock Quotes for Machine Learning on B3 (1995–2020)

> **Cardoso, F., Malska, J., Ramiro, P., Lucca, G., Borges, E. N., Mattos, V. d., & Berri, R. (2021).**
> *Bovdb: The data set of stock quotes for machine learning on all companies from B3 between 1995 and 2020.*
> In Proceedings of the Brazilian Symposium on Databases — Dataset Showcase (SBBD). SBC.

---

## Overview

**BovDB v1.0** is the original version of the BovDB dataset, published at the **SBBD 2021 Dataset Showcase**. It contains **daily OHLCV historical quotes with corporate action adjustment factors** for all equities traded on the Brazilian Stock Exchange (B3) from **1995 to 2020**.

This version focuses exclusively on **daily-resolution data** and provides the foundation for time-series forecasting, econometric modeling, and machine learning benchmarks on Brazilian equities.

---

## 🔽 Download the Database

All archives are included directly in this directory (no external download required):

| File | Format | Size |
|---|---|---|
| [`DataBase.db.zip`](DataBase.db.zip) | SQLite database (compressed) | ~57 MB |
| [`DataBase.zip`](DataBase.zip) | SQLite database (alternative archive) | ~92 MB |
| [`DataBase_CSV.zip`](DataBase_CSV.zip) | CSV flat-file exports of all tables | ~49 MB |
| [`DataBase_JSON.zip`](DataBase_JSON.zip) | JSON structured records of all tables | ~94 MB |

### Quick Start

1. Download and extract one of the archives above (SQLite recommended).
2. Place `DataBase.db` at `DataBase/DataBase.db` (relative to the repository root).
3. Query directly with any SQLite client, Python, R, or the `bovdb` SDK.

---

## Database Schema (V1)

V1 contains **3 tables** — there is **no intraday data** in this version.

| Table | Description | Primary Key |
|---|---|---|
| `company` | Listed companies on B3 with sectoral classification | `id_company` |
| `ticker` | B3 tickers (ON, PN, UNT, BDRs) linked to companies | `id_ticker` |
| `price` | Daily OHLCV quotes with cumulative split/bonus `factor` | `(id_ticker, date)` |

### Table `company`

| Column | Type | Description |
|---|---|---|
| `id_company` | `INTEGER` | Primary Key. Unique company identifier. |
| `name` | `TEXT` | Full corporate name (e.g., `PETROLEO BRASILEIRO S.A. PETROBRAS`). |
| `sector` | `TEXT` | B3 Economic Sector classification. |
| `subsector` | `TEXT` | B3 Subsector classification. |
| `segment` | `TEXT` | B3 Activity Segment. |

### Table `ticker`

| Column | Type | Description |
|---|---|---|
| `id_ticker` | `INTEGER` | Primary Key. Unique ticker identifier. |
| `cd_ticker` | `TEXT` | Ticker symbol on B3 (e.g., `PETR4`, `VALE3`). |
| `id_company` | `INTEGER` | Foreign Key → `company(id_company)`. |
| `type` | `TEXT` | Share class: `ON` (Common), `PN` (Preferred), `UNT` (Units), `DRN` (BDRs). |

### Table `price` (Daily Quotes)

| Column | Type | Description |
|---|---|---|
| `id_ticker` | `INTEGER` | Foreign Key → `ticker(id_ticker)`. |
| `date` | `TEXT` | Trading date (`YYYY-MM-DD`). |
| `open` | `REAL` | Opening price in BRL (R$). |
| `high` | `REAL` | Highest traded price in BRL (R$). |
| `low` | `REAL` | Lowest traded price in BRL (R$). |
| `close` | `REAL` | Closing settlement price in BRL (R$). |
| `volume` | `REAL` | Total financial trading volume in BRL (R$). |
| `trades` | `INTEGER` | Total number of executed trades. |
| `factor` | `REAL` | Cumulative adjustment factor for splits, inplits, and bonuses. Default `1.0`. |

> **Price Adjustment Formula**:
> $$\text{Price}_{\text{adjusted}}(t) = \frac{\text{Price}_{\text{nominal}}(t)}{\text{factor}(t)}$$

---

## ⚠️ Limitations of V1 (addressed in V2)

| Limitation | Resolved in V2? |
|---|---|
| Daily data only — no intraday resolution | ✅ V2 adds `price5` table (5-min bars) |
| Coverage ends in 2020 | ✅ V2 extends to mid-2024 |
| No permanent DOI for citation | ✅ V2 published on [Harvard Dataverse](https://doi.org/10.7910/DVN/TMB4IG) |
| Distribution via GitHub LFS / ZIP only | ✅ V2 adds Harvard Dataverse + Dropbox mirrors |

> 💡 **Upgrade to V2**: If you need intraday data or extended coverage beyond 2020, see [`BovdbV2/`](../BovdbV2/).

---

## Integrity Verification

SHA-256 checksums are available in [`checksums.sha256`](checksums.sha256) for verifying archive integrity:

```bash
# Verify all archives
sha256sum -c checksums.sha256
```

Structured metadata is available in [`manifest.json`](manifest.json).

---

## Citation (V1)

```bibtex
@inproceedings{cardoso2021bovdb,
  title     = {Bovdb: The data set of stock quotes for machine learning on all companies from B3 between 1995 and 2020},
  author    = {Cardoso, Fabian and Malska, Juan and Ramiro, Paulo and Lucca, Giancarlo and Borges, Eduardo N and Mattos, Viviane de and Berri, Rafael},
  booktitle = {Proceedings of the Brazilian Symposium on Databases - Dataset Showcase},
  year      = {2021},
  organization = {SBC}
}
```

---

## License

This dataset is licensed under [Creative Commons Attribution-NonCommercial 4.0 International](../LICENSE.md) (CC BY-NC 4.0).
