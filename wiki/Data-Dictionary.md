# 📖 BovDB Data Dictionary

Complete reference schema, data types, constraints, and descriptions for all tables in the BovDB SQLite database.

---

## 1. Table `company`
Stores listed corporate entities on B3 and official sectoral classifications.

| Column | Type | Nullable | Primary Key | Description |
| :--- | :--- | :--- | :--- | :--- |
| `id_company` | `INTEGER` | No | Yes | Unique company identifier |
| `name` | `TEXT` | No | No | Official corporate name |
| `sector` | `TEXT` | Yes | No | B3 Economic Sector |
| `subsector` | `TEXT` | Yes | No | B3 Subsector classification |
| `segment` | `TEXT` | Yes | No | B3 Activity Segment |

---

## 2. Table `ticker`
Stores individual tradable tickers (assets) linked to companies.

| Column | Type | Nullable | Primary Key | Description |
| :--- | :--- | :--- | :--- | :--- |
| `id_ticker` | `INTEGER` | No | Yes | Unique ticker identifier |
| `cd_ticker` | `TEXT` | No | No | B3 ticker symbol (e.g., `PETR4`, `VALE3`) |
| `id_company` | `INTEGER` | Yes | No (FK) | Reference to `company(id_company)` |
| `type` | `TEXT` | Yes | No | Share class (`ON`, `PN`, `UNT`, `DRN`) |

---

## 3. Table `price` (Daily Quotes)
Daily historical OHLCV quotes and corporate action adjustment factors.

| Column | Type | Nullable | Description |
| :--- | :--- | :--- | :--- |
| `id_ticker` | `INTEGER` | No | Foreign Key referencing `ticker(id_ticker)` |
| `date` | `TEXT` | No | Date formatted as `YYYY-MM-DD` |
| `open` | `REAL` | No | Nominal opening price (R$) |
| `high` | `REAL` | No | Nominal daily high price (R$) |
| `low` | `REAL` | No | Nominal daily low price (R$) |
| `close` | `REAL` | No | Nominal daily close price (R$) |
| `volume` | `REAL` | Yes | Traded financial volume (R$) |
| `trades` | `INTEGER` | Yes | Total number of executed trades |
| `factor` | `REAL` | No | Split/inplit multiplier factor (default `1.0`) |

> 📐 **Adjusted Price Formula**:
> $$\text{Price}_{\text{adjusted}} = \frac{\text{Price}_{\text{nominal}}}{\text{factor}}$$

---

## 4. Table `price5` (5-Minute Intraday Quotes)
High-frequency 5-minute aggregated OHLCV intraday candlestick bars.

| Column | Type | Nullable | Description |
| :--- | :--- | :--- | :--- |
| `id_ticker` | `INTEGER` | No | Foreign Key referencing `ticker(id_ticker)` |
| `date` | `TEXT` | No | Trading date (`YYYY-MM-DD`) |
| `time` | `TEXT` | No | Bar start time in `HH:MM:SS` format (BRT / UTC-3) |
| `open` | `REAL` | No | Bar opening price (R$) |
| `high` | `REAL` | No | Bar high price (R$) |
| `low` | `REAL` | No | Bar low price (R$) |
| `close` | `REAL` | No | Bar closing price (R$) |
| `volume` | `REAL` | Yes | Traded volume in 5-minute window (R$) |
| `trades` | `INTEGER` | Yes | Number of trades in 5-minute window |
