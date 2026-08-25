# 🔬 Data Provenance & Reproducibility

Guidelines for empirical benchmarks and academic research with BovDB.

---

## 1. Corporate Event Adjustments
Raw market prices do not account for stock splits or reverse splits.
To compute true economic returns and technical indicators, always adjust nominal prices:

$$\text{Price}_{\text{adj}} = \frac{\text{Price}_{\text{nominal}}}{\text{factor}}$$

```python
# Returns adjusted DataFrame automatically
df_adj = bovdb.get_daily_prices(conn, ticker="PETR4", adjusted=True)
```

---

## 2. Seed Fixing in ML Benchmarks
To ensure exact reproduction of neural networks or tree-based ensemble models across experiments:
```python
import random
import numpy as np

random.seed(42)
np.random.seed(42)
```
