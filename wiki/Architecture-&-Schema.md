# 🏛️ Architecture & Schema Design

## 1. Relational Architecture

BovDB uses a normalized SQLite schema designed for maximum query speed and minimal dependency footprint.

```mermaid
erDiagram
    COMPANY ||--o{ TICKER : issues
    TICKER ||--o{ PRICE : has_daily_quotes
    TICKER ||--o{ PRICE5 : has_intraday_quotes

    COMPANY {
        int id_company PK
        string name
        string sector
        string subsector
        string segment
    }

    TICKER {
        int id_ticker PK
        string cd_ticker
        int id_company FK
        string type
    }

    PRICE {
        int id_ticker FK
        date date
        float open
        float high
        float low
        float close
        float volume
        int trades
        float factor
    }

    PRICE5 {
        int id_ticker FK
        date date
        time time
        float open
        float high
        float low
        float close
        float volume
        int trades
    }
```

---

## 2. High-Frequency Layer Integration

The database unifies both daily and intraday resolutions:
1. **Daily Layer (`price`)**: Ideal for multi-decade backtests, asset allocation models, and long-term risk parity strategies (1995 to present).
2. **Intraday Layer (`price5`)**: Ideal for microstructural analysis, order book volatility estimation, and high-frequency algorithmic execution modeling.
