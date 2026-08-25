# BovDB Architecture & Design

## 1. Overview

**BovDB** is a relational database designed to store, organize, and serve historical and intraday financial market data from the Brazilian Stock Exchange (**B3**). Built as an open-access resource for machine learning and econometric research, BovDB provides clean, pre-processed time series that account for corporate events (stock splits, inplit, and dividends) via adjustment factors.

```mermaid
graph TD
    subgraph Data Sources
        B3Raw[B3 Historical Quotations]
        B3Intra[B3 Intraday 5-Min Feeds]
        B3Corp[Corporate Actions & Factors]
    end

    subgraph Relational Engine
        DB[(BovDB SQLite Database)]
        T_Comp[company table]
        T_Tick[ticker table]
        T_Price[price table - Daily]
        T_Price5[price5 table - 5min Intraday]
    end

    subgraph Access & Research Layer
        Pkg[src/bovdb Python Module]
        Codes[Codes / Scripts]
        Notebooks[Jupyter Notebooks]
        ML[Machine Learning & Econometrics]
    end

    B3Raw --> DB
    B3Intra --> DB
    B3Corp --> DB

    DB --- T_Comp
    DB --- T_Tick
    DB --- T_Price
    DB --- T_Price5

    DB --> Pkg
    Pkg --> Codes
    Pkg --> Notebooks
    Notebooks --> ML
    Codes --> ML
```

---

## 2. Relational Schema Architecture

The database is implemented in **SQLite**, balancing zero-configuration portability, fast read performance, and standard SQL support.

### Entities and Relationships

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

## 3. Data Flow & Integration

1. **Extraction and Ingestion**: Raw daily files from B3 and intraday 5-minute ticks are harmonized into relational tables with consistent data types (`INTEGER`, `TEXT`, `REAL`).
2. **Adjustment Factor Application**: Prices in the `price` table are stored in nominal terms along with a `factor` multiplier. Adjusted prices are computed as:
   $$\text{Price}_{\text{adjusted}} = \frac{\text{Price}_{\text{nominal}}}{\text{factor}}$$
3. **Consumption**: End-user research workflows query the database directly using SQL or via the `bovdb` Python helper module (`src/bovdb`).
