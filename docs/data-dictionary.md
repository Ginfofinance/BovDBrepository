# BovDB Data Dictionary

This document specifies the complete schema, data types, constraints, and descriptions for all tables in the **BovDB** database.

---

## 1. Table `company`

Stores general information and sector classifications for listed companies on B3.

| Column | Type | Nullable | Description |
| :--- | :--- | :--- | :--- |
| `id_company` | `INTEGER` | No | Primary Key. Unique identifier for the listed company. |
| `name` | `TEXT` | No | Full corporate name of the company (e.g., `PETROLEO BRASILEIRO S.A. PETROBRAS`). |
| `sector` | `TEXT` | Yes | B3 Economic Sector classification (e.g., `Petróleo, Gás e Biocombustíveis`). |
| `subsector` | `TEXT` | Yes | B3 Subsector classification (e.g., `Petróleo, Gás e Biocombustíveis`). |
| `segment` | `TEXT` | Yes | B3 Activity Segment (e.g., `Exploração, Refino e Distribuição`). |

---

## 2. Table `ticker`

Stores individual tradable tickers (assets) associated with each company.

| Column | Type | Nullable | Description |
| :--- | :--- | :--- | :--- |
| `id_ticker` | `INTEGER` | No | Primary Key. Unique identifier for the ticker. |
| `cd_ticker` | `TEXT` | No | Asset ticker symbol on B3 (e.g., `PETR4`, `VALE3`, `ITUB4`). |
| `id_company` | `INTEGER` | Yes | Foreign Key referencing `company(id_company)`. |
| `type` | `TEXT` | Yes | Share class type: `ON` (Common), `PN` (Preferred), `UNT` (Units), `DRN` (BDRs). |

---

## 3. Table `price` (Daily Quotes)

Stores historical daily OHLCV quotes and corporate adjustment factors.

| Column | Type | Nullable | Description |
| :--- | :--- | :--- | :--- |
| `id_ticker` | `INTEGER` | No | Foreign Key referencing `ticker(id_ticker)`. |
| `date` | `TEXT` | No | Trading date formatted as `YYYY-MM-DD`. |
| `open` | `REAL` | No | Opening price in BRL (R$). |
| `high` | `REAL` | No | Highest traded price of the day in BRL (R$). |
| `low` | `REAL` | No | Lowest traded price of the day in BRL (R$). |
| `close` | `REAL` | No | Closing settlement price in BRL (R$). |
| `volume` | `REAL` | Yes | Total financial trading volume in BRL (R$). |
| `trades` | `INTEGER` | Yes | Total number of executed trades for the day. |
| `factor` | `REAL` | No | Adjustment factor for corporate actions (splits, inplits, bonuses). Default `1.0`. |

> **Note on Factor**: To obtain the split-adjusted price:
> $$\text{adjusted\_price} = \frac{\text{nominal\_price}}{\text{factor}}$$

---

## 4. Table `price5` (5-Minute Intraday Quotes)

Stores 5-minute aggregated OHLCV intraday candlestick bars.

| Column | Type | Nullable | Description |
| :--- | :--- | :--- | :--- |
| `id_ticker` | `INTEGER` | No | Foreign Key referencing `ticker(id_ticker)`. |
| `date` | `TEXT` | No | Trading session date (`YYYY-MM-DD`). |
| `time` | `TEXT` | No | Bar start time in `HH:MM:SS` format (BRT / UTC-3). |
| `open` | `REAL` | No | Bar opening price in BRL (R$). |
| `high` | `REAL` | No | Bar maximum price in BRL (R$). |
| `low` | `REAL` | No | Bar minimum price in BRL (R$). |
| `close` | `REAL` | No | Bar closing price in BRL (R$). |
| `volume` | `REAL` | Yes | Financial volume traded within the 5-minute window. |
| `trades` | `INTEGER` | Yes | Number of trades within the 5-minute window. |
