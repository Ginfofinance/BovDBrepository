# 📊 Dataset Versions & Changelog

BovDB follows a structured versioning approach preserving historical scientific reproducibility while delivering modern tools for high-frequency financial modeling.

---

## 📈 Comparison Matrix

| Attribute | **BovDB v1.0** (2021) | **BovDB v2.0** (2024) | **BovDB v3.0** (2026+) |
| :--- | :--- | :--- | :--- |
| **Temporal Range** | 1995 – 2020 | 1995 – 2024 | 1995 – Present |
| **Market Scope** | All B3 Listed Equities | All B3 Listed Equities | All B3 Listed Equities |
| **Daily OHLCV** | ✅ Yes (`price` table) | ✅ Yes (`price` table) | ✅ Yes (`price` table) |
| **5-Min Intraday** | ❌ No | ✅ Yes (`price5` table) | ✅ Yes (`price5` table) |
| **Adjustment Factors** | ✅ Yes | ✅ Yes | ✅ Yes (Automatic in SDK) |
| **Distribution Formats** | CSV, JSON, SQLite `.zip` | SQLite RAR (DropBox) | SQLite RAR/ZIP (Multi-mirror) |
| **Python Library** | Standalone scripts | Standalone scripts | Modular `bovdb` SDK |
| **CI/CD & Testing** | None | None | GitHub Actions (Python 3.10–3.12) |
| **Packaging** | Manual copy | Manual copy | `pyproject.toml` & GitHub Packages |

---

## 📜 Version History

### Version 3.0.0 (August 2026)
* Reorganized the entire repository into a unified single-repository architecture.
* Released the `bovdb` Python package for clean, typed SQL data fetching and automated visualizations.
* Added CI/CD automated test workflows and GitHub Packages integration.
* Created comprehensive documentation: ER architecture, complete data dictionary, and reproducibility guidelines.

### Version 2.0.0 (Late 2024)
* Extended daily quote coverage to mid-2024.
* Introduced high-frequency 5-minute intraday quotes (`price5` table).
* Added Plotly-based interactive intraday candlestick visualization.
* Released new extrema detection algorithm for tops and bottoms.

### Version 1.0.0 (April 2021)
* Initial publication at the XXXVI Brazilian Symposium on Databases (*SBBD 2021 - Dataset Showcase*).
* First open-access structured dataset covering all B3 companies from 1995 to 2020.
* Multi-format export: CSV, JSON, SQLite.
