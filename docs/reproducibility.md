# Data Provenance & Reproducibility Guide

## 1. Data Integrity and Verification

**BovDB** provides historical and intraday financial market time series formatted specifically for reproducible empirical research, quantitative modeling, and machine learning.

To ensure consistency and comparability across academic studies:

1. **Deterministic Processing**: When training ML models or computing econometric statistics, always fix pseudo-random generator seeds (e.g. `numpy.random.seed(42)`).
2. **Adjustment Factor Handling**: Stock splits, reverse splits (inplits), and bonuses affect raw nominal prices. In the database, the `price` table includes a `factor` column.
   - For return calculations and technical indicators, use adjusted prices:
     $$\text{Price}_{\text{adj}} = \frac{\text{Price}}{\text{factor}}$$
3. **Database File Placement**: Place the extracted database `DataBase.db` inside the `DataBase/` folder at the repository root, or configure the path via the `BOVDB_PATH` environment variable.

---

## 2. Directory Layout & Isolation

To keep repository clones lightweight and avoid accidentally committing massive binary datasets:
- The `DataBase/` directory is monitored by Git, but `.db` binary files are strictly excluded in `.gitignore`.
- Analysis outputs (PDF charts, CSV exports, intermediate models) are written to local directories excluded from version control.

---

## 3. Computational Environment

We recommend managing dependencies within a Python virtual environment:

```bash
# Create virtual environment
python -m venv .venv

# Activate
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# Install locked dependencies
pip install -r requirements.txt
```
