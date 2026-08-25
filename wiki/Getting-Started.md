# 🚀 Getting Started with BovDB

This guide walks you through setting up your environment, downloading the SQLite database, and running your first financial queries and visualizations.

---

## 1. Environment Setup

Clone the repository and set up a Python virtual environment:

```bash
# Clone the repository
git clone https://github.com/Ginfofinance/BovDBrepository.git
cd BovDBrepository

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Linux / macOS:
source .venv/bin/activate

# Install dependencies and local bovdb package
pip install -r requirements.txt
pip install -e .
```

---

## 2. Database Download and Placement

1. Open [`BovdbV3/link_database.txt`](https://github.com/Ginfofinance/BovDBrepository/blob/main/BovdbV3/link_database.txt) to get the latest download mirror link.
2. Download the compressed archive `Database_define.rar` (or `.zip`).
3. Extract the SQLite database file as `DataBase.db` (or `Database_define.db`).
4. Place the extracted file inside the `DataBase/` folder in the repository root:
   ```text
   BovDBrepository/
   └── DataBase/
       ├── .gitkeep
       ├── README.md
       └── DataBase.db   <-- Place your SQLite file here
   ```

> 💡 **Custom Path Option**: If you store the database on an external drive or specific path, set the environment variable:
> ```bash
> export BOVDB_PATH="/path/to/your/DataBase.db"
> ```

---

## 3. Running Example Scripts

Try executing the provided benchmark scripts in `Codes/`:

* **Daily Candlesticks Chart**:
  ```bash
  python Codes/daily_candlesticks_chart.py
  ```
* **Annual Mean & Standard Deviation**:
  ```bash
  python Codes/annual_mean_and_standard_deviation_graph.py
  ```
* **5-Minute High-Frequency Intraday Chart**:
  ```bash
  python Codes/intraday_5min_candlestick.py
  ```
* **Jupyter Top & Bottom Detection Notebook**:
  ```bash
  jupyter notebook Codes/low_and_bottom.ipynb
  ```
