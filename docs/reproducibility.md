# Data Reproducibility & Benchmark Standards

## 1. Reproducible Financial Modeling

**BovDB** provides historical and intraday financial market time series formatted specifically for reproducible empirical research, quantitative modeling, and machine learning.

To ensure consistency and comparability across academic studies:

1. **Deterministic Random Seeds**: When training ML models (e.g. XGBoost, PyTorch, TensorFlow) or computing bootstrap statistics, always fix pseudo-random generator seeds:
   ```python
   import random
   import numpy as np

   random.seed(42)
   np.random.seed(42)
   ```

2. **Corporate Action Adjustment Handling**: Stock splits, reverse splits (*inplits*), and bonuses affect raw nominal prices. In the database, the `price` table includes a `factor` column.
   - For return calculations and technical indicators, use adjusted prices:
     $$\text{Price}_{\text{adj}} = \frac{\text{Price}}{\text{factor}}$$
   - The Python SDK provides this automatically:
     ```python
     df = bovdb.get_daily_prices(conn, ticker="PETR4", adjusted=True)
     ```

3. **Data Provenance & Lineage**: For the complete origin and transformation lineage of the raw B3 COTAHIST and intraday feeds, refer to the [Data Provenance Guide](provenance.md).

---

## 2. Environment Isolation & Dependencies

We recommend managing dependencies within a Python virtual environment:

```bash
# Create virtual environment
python -m venv .venv

# Activate
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# Install base package
pip install -e .

# Or install with visualization and analysis extras:
pip install -e ".[viz,analysis,dev]"
```
