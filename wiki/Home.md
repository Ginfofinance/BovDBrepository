# 📚 Welcome to the BovDB Wiki

**BovDB** (*Bovespa Database*) is an open-access, high-performance relational dataset and Python toolkit containing historical stock quotes and high-frequency intraday data from the Brazilian Stock Exchange (**B3**), purpose-built for machine learning benchmarks, quantitative finance, econometric modeling, and algorithmic trading research.

---

## 🧭 Wiki Quick Navigation

| Section | Description | Target Link |
| :--- | :--- | :--- |
| 🚀 **Getting Started** | Step-by-step setup, Python environment, and database placement | [Getting Started](Getting-Started) |
| 📊 **Dataset Versions** | Scope, periods, and features comparison (v1.0, v2.0, v3.0) | [Versions & Changelog](Versions-&-Changelog) |
| 📖 **Data Dictionary** | Complete schema for `company`, `ticker`, `price`, and `price5` | [Data Dictionary](Data-Dictionary) |
| 🏛️ **Architecture & Schema** | Relational model, ER diagram, and factor adjustment methodology | [Architecture & Schema](Architecture-&-Schema) |
| 🐍 **Python API Reference** | Complete documentation for queries, loaders, and visualizers | [Python API Reference](Python-API-Reference) |
| 🔬 **Reproducibility Guide** | Benchmark protocols, seed fixing, and empirical standards | [Reproducibility & Benchmarks](Reproducibility-&-Benchmarks) |
| ❓ **FAQ & Troubleshooting** | Common questions, installation tips, and troubleshooting | [FAQ & Troubleshooting](FAQ-&-Troubleshooting) |

---

## 🌟 Key Features

* **Complete B3 Equity Coverage**: Common shares (`ON`), Preferred shares (`PN`), Units (`UNT`), and Brazilian Depositary Receipts (`BDRs`).
* **Multi-Resolution Time Series**:
  * **Daily Historical OHLCV**: 1995 to Present.
  * **Intraday 5-Minute OHLCV**: High-frequency candlestick bars (`price5`).
* **Corporate Event Multipliers**: Dedicated `factor` column adjusting for stock splits, reverse splits (*inplits*), and stock dividends.
* **Portable Zero-Config Storage**: Single-file SQLite database (`DataBase.db`) requiring no database server setup.
* **Modern Python SDK**: Typed helper functions in `bovdb` for instant querying with pandas and interactive visualization with mplfinance/Plotly.

---

## 📊 Dataset Versions at a Glance

| Version | Period | Primary Resolution | Main Highlights |
| :--- | :--- | :--- | :--- |
| **BovDB v1.0** | 1995 – 2020 | Daily OHLCV | Original dataset presented at SBBD 2021. Formats: CSV, JSON, SQLite. |
| **BovDB v2.0** | 1995 – 2024 | Daily + 5-Min Intraday | Extended daily history + introduction of `price5` high-frequency table. |
| **BovDB v3.0** | 1995 – Present | Daily + 5-Min Intraday | Modular `bovdb` Python library, automated CI/CD, and multi-mirror downloads. |

---

## ⚡ Quick Example

```python
import bovdb

# Connect to database
conn = bovdb.get_connection()

# Load split-adjusted daily prices for Petrobras (PETR4)
df_petr4 = bovdb.get_daily_prices(conn, ticker="PETR4", start_date="2023-01-01", end_date="2024-06-30", adjusted=True)

# Generate candlestick chart
bovdb.plot_candlestick(df_petr4, ticker_name="PETR4 (Adjusted)")

conn.close()
```

---

## 🎓 Research Group & Affiliation

This project is developed and maintained by the **Grupo de Pesquisa em Informática na Gestão da Informação e Finanças (GINFO)**:
* **PPGMC** — Programa de Pós-Graduação em Modelagem Computacional
* **C3** — Centro de Ciências Computacionais
* **IMEF** — Instituto de Matemática, Estatística e Física
* **FURG** — Universidade Federal do Rio Grande

**Official Repository**: [github.com/Ginfofinance/BovDBrepository](https://github.com/Ginfofinance/BovDBrepository)
