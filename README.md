# BovDB: Stock Quotes Dataset for Machine Learning on B3 Equities

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](LICENSE.md)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](pyproject.toml)
[![Database](https://img.shields.io/badge/Database-SQLite-003B57.svg?logo=sqlite&logoColor=white)](docs/architecture.md)
[![B3 Equities](https://img.shields.io/badge/Market-B3%20Brazil-004B87.svg)](https://www.b3.com.br/)
[![CI Checks](https://github.com/Ginfofinance/BovDBrepository/actions/workflows/ci.yml/badge.svg)](https://github.com/Ginfofinance/BovDBrepository/actions)
[![DOI](https://img.shields.io/badge/DOI-10.7910%2FDVN%2FTMB4IG-blue.svg)](https://doi.org/10.7910/DVN/TMB4IG)

---

**Andrey Vinicius Souza, Fabian Corrêa Cardoso, Juan Malska, Paulo Ramiro, Giancarlo Lucca, Eduardo N. Borges, Viviane de Mattos, Rafael Berri**

* **Grupo de Pesquisa em Informática na Gestão da Informação e Finanças (GINFO)**
* **Programa de Pós-Graduação em Modelagem Computacional (PPGMC)** — Universidade Federal do Rio Grande (FURG)
* **Centro de Ciências Computacionais (C3)** — Universidade Federal do Rio Grande (FURG)
* **Instituto de Matemática, Estatística e Física (IMEF)** — Universidade Federal do Rio Grande (FURG)
* **Contato**: `{andreyvinicius, fabiancorrea, giancarlo.lucca, eduardoborges, vivianemattos, rafaelberri}@furg.br`

---

## Overview

**BovDB** is an open-access, relational dataset and Python toolkit of historical stock quotes and high-frequency intraday data covering all companies listed on the Brazilian Stock Exchange (**B3**), designed for machine learning benchmarks, econometric modeling, time-series forecasting, and algorithmic trading research.

### Key Capabilities
- **Complete Equity Coverage**: Covers all tickers traded on B3 across common (ON), preferred (PN), units (UNT), and Brazilian Depositary Receipts (BDRs).
- **Corporate Action Adjustments**: Accounts for stock splits, reverse splits (inplits), and bonuses via dedicated `factor` multipliers.
- **Multi-Resolution Data**: Includes daily historical OHLCV series (1995–Present) along with high-frequency 5-minute intraday bars (`price5`).
- **Safe Read-Only Python SDK**: Modular `bovdb` Python package opening SQLite connections in strict read-only mode by default to prevent database corruption.
- **Zero-Configuration Relational Storage**: Stored in a high-performance, single-file SQLite database with straightforward Python integration.

---

## Dataset Versions & Scope

| Version | Status / Folder | Period | Resolution | Features & Archive Formats |
| :--- | :--- | :--- | :--- | :--- |
| **BovDB v1.0** | [`BovdbV1/`](BovdbV1/) | 1995 – 2020 | Daily | All B3 equities, daily OHLCV, adjustment factors. Formats: CSV, JSON, SQLite (`.zip`). Published at SBBD 2021. |
| **BovDB v2.0** | [`BovdbV2/`](BovdbV2/) — [Harvard Dataverse](https://doi.org/10.7910/DVN/TMB4IG) | 1995 – 2024 | Daily + Intraday | Daily historical quotes + 5-min intraday `price5` (Jan–Jun 2024). **Official published version** (DOI: [10.7910/DVN/TMB4IG](https://doi.org/10.7910/DVN/TMB4IG)). |
| **BovDB v3.0** | 🚧 In Development — [`BovdbV3/`](BovdbV3/) | 1995 – Present | Daily + Intraday | Modular `bovdb` Python package, CI/CD, complete schema dictionary, multi-mirror links. |

---

## Quick Start

### 1. Clone & Environment Setup

```bash
git clone https://github.com/Ginfofinance/BovDBrepository.git
cd BovDBrepository

# Create and activate virtual environment
python -m venv .venv

# On Windows:
.venv\Scripts\activate
# On Linux / macOS:
source .venv/bin/activate

# Install base package with visualization tools:
pip install -e ".[viz,analysis,dev]"
```

### 2. Download the Database

1. Open [`BovdbV3/link_database.txt`](BovdbV3/link_database.txt) (or [`BovdbV2/link_database.txt`](BovdbV2/link_database.txt)) to access download links.
2. Download and extract `Database_define.rar` (or `.zip`).
3. Place the extracted SQLite database file inside the `DataBase/` folder:
   ```text
   DataBase/DataBase.db
   ```
*(Optional)* You can also set a custom path using the `BOVDB_PATH` environment variable.

### 3. Run Example Scripts

- **Daily Candlestick Chart (with and without factor adjustment)**:
  ```bash
  python Codes/daily_candlesticks_chart.py
  ```

- **Annual Mean and Standard Deviation Graph**:
  ```bash
  python Codes/annual_mean_and_standard_deviation_graph.py
  ```

- **Interactive 5-Minute Intraday Candlestick Chart**:
  ```bash
  python Codes/intraday_5min_candlestick.py
  ```

- **Top & Bottom Extrema Detection (Jupyter Notebook)**:
  ```bash
  jupyter notebook Codes/low_and_bottom.ipynb
  ```

---

## Python API Example

You can query the dataset directly in your research workflows using the `bovdb` package:

```python
import bovdb

# Automatically connects to DataBase/DataBase.db in safe read-only mode
conn = bovdb.get_connection()

# 1. Fetch split-adjusted daily prices for Petrobras (PETR4)
df_daily = bovdb.get_daily_prices(conn, ticker="PETR4", start_date="2023-01-01", end_date="2024-06-30", adjusted=True)
bovdb.plot_candlestick(df_daily, ticker_name="PETR4 (Adjusted)")

# 2. Fetch 5-minute intraday quotes
df_intra = bovdb.get_intraday_5min(conn, ticker="PETR4", start_date="2024-06-26", end_date="2024-06-26")
bovdb.plot_intraday_5min(df_intra, day="2024-06-26", ticker_name="PETR4")

conn.close()
```

---

## Documentation

- [Architecture & Design](docs/architecture.md) — Relational ER model and table structures.
- [Data Dictionary](docs/data-dictionary.md) — Detailed table schemas (`company`, `ticker`, `price`, `price5`).
- [Data Provenance & Lineage](docs/provenance.md) — Origin feeds (B3/CVM), data harmonization, and quality gates.
- [Data Reproducibility Standards](docs/reproducibility.md) — Protocols for machine learning benchmarks and random seed fixing.
- [Repository Governance](docs/governance.md) — Branch protection rules, PR reviews, and semantic commit standards.
- [Contributing Guide](CONTRIBUTING.md) — How to propose enhancements and submit pull requests.
- [Code of Conduct](CODE_OF_CONDUCT.md) — Community standards and academic integrity.
- [Security Policy](SECURITY.md) — Guidelines for reporting vulnerabilities.

---

## Citation

If you use **BovDB** in scientific publications or academic projects, please cite:

### BovDB V2 (Harvard Dataverse — Official Published Version)

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

### BovDB V1 (SBBD 2021)

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

This dataset and accompanying software are licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](LICENSE.md) (CC BY-NC 4.0).
